# -*- coding: utf-8 -*-

# system dependencies
import os, subprocess
from os.path import join, dirname, realpath
import json
import re
# tornado dependencies
import tornado.ioloop
from tornado.web import RequestHandler, HTTPError, Application, asynchronous, authenticated
from tornado.httpclient import AsyncHTTPClient
from tornado import gen
import tornado.escape
from tornado.options import define, options, parse_command_line
from jinja2 import Environment, PackageLoader
from mimetypes import guess_type
from .urls import urls
# visualization dependencies
from .version import __version__
# sbaas dependencies
from sbaas.data import sbaas_settings as sbaas_settings
from sbaas.analysis.visualization import visualization_io
from sbaas.analysis.analysis_stage01_ale import stage01_ale_io
from sbaas.analysis.analysis_stage01_physiology import stage01_physiology_io
from sbaas.analysis.analysis_stage01_resequencing import stage01_resequencing_io
from sbaas.analysis.analysis_stage02_isotopomer import stage02_isotopomer_io
from sbaas.analysis.analysis_stage02_quantification import stage02_quantification_io
from sbaas.analysis.analysis_stage02_resequencing import stage02_resequencing_io
from sbaas.models.models_base import Session

# set up jinja2 template location
env = Environment(loader=PackageLoader('visualization', 'templates'))

# set directory to server
directory = dirname(realpath(__file__))
NO_CACHE = True
PORT = 8080
PUBLIC = False # localhost
#PUBLIC = True # web

# initialize a global session:
session = Session();

def run(port=PORT, public=PUBLIC):
    global PORT
    global PUBLIC
    PORT = port
    PUBLIC = public
    print('serving directory %s on port %d' % (directory, PORT))
    application.listen(port, None if public else "localhost")
    try:
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        print("Thank you!  Come again!")

def stop():
    tornado.ioloop.IOLoop.instance().stop()

class BaseHandler(RequestHandler):
    def serve_path(self, path):
        # make sure the path exists
        if not os.path.isfile(path):
            raise HTTPError(404)
        # serve it
        with open(path, "rb") as file:
            data = file.read()
        # set the mimetype
        self.set_header("Content-Type", guess_type(path, strict=False)[0])
        self.serve(data)
        
    def serve(self, data):
        if (NO_CACHE):
            self.set_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.set_header('Access-Control-Allow-Origin', '*')
        self.write(data)
        self.finish();

    def get_login_url(self):
        return "/login"

    def get_current_user(self):
        user_json = self.get_secure_cookie("user")
        if user_json:
            return tornado.escape.json_decode(user_json)
        else:
            return None

class LoginHandler(BaseHandler):

    def get(self):
        # render the template
        template = env.get_template('login.html')
        source = 'local'
        url = urls();
        data = template.render(d3=url.get_url('d3', source),
                               boot_css=url.get_url('boot_css', source),
                               index_css=url.get_url('index_css', source),
                               logo=url.get_url('logo1', source),
                               github=url.get_url('github'),
                               version=__version__,
                               #next=self.get_argument("next","/"),
                               web_version=False)
        
        self.set_header("Content-Type", "text/html")
        self.serve(data)
        #self.render("login.html", next=self.get_argument("next","/"))

    def post(self):
        username = self.get_argument("username", "")
        password = self.get_argument("password", "")
        # The authenticate method should match a username and password
        # to a username and password hash in the database users table.
        login = {};
        login['language']='biochemistry';
        print(username, password)
        auth = False;
        if username in login and login[username]==login['language']: auth = True;
        if auth:
            self.set_current_user(username)
            self.redirect("/")
        else:
            error_msg = "?error=" + tornado.escape.url_escape("Login incorrect.")
            self.redirect("/login" + error_msg)

    def set_current_user(self, user):
        if user:
            self.set_secure_cookie("user", tornado.escape.json_encode(user))
        else:
            self.clear_cookie("user")

class LogoutHandler(BaseHandler):

    def get(self):
        self.clear_cookie("user")
        self.redirect("/login")

class IndexHandler(BaseHandler):
    @asynchronous
    @gen.coroutine
    @authenticated
    def get(self):
        url = urls();
        #response = yield gen.Task(AsyncHTTPClient().fetch,
        #                          '/'.join([url.get_url('index_filter', source='local',protocol='https')]));
        #json_data = response.body if response.body is not None else json.dumps(None)
        with open(sbaas_settings.visualization_resources+'/'+url.get_url('index_filter', source='local',protocol='https'), "r") as file:
            json_data = file.read();
        # render the template
        template = env.get_template('index.html')
        source = 'local'
        data = template.render(d3=url.get_url('d3', source),
            boot_css=url.get_url('boot_css', source),
            boot_js=url.get_url('boot_js', source),
            index_js=url.get_url('index_js', source),
            index_css=url.get_url('index_css', source),
            jquery=url.get_url('jquery', source),
            logo1=url.get_url('logo3', source),
            logo2=url.get_url('logo4', source),
            logo3=url.get_url('logo5', source),
            logo4=url.get_url('logo6', source),
            logo5=url.get_url('logo7', source),
            github=url.get_url('github'),
            #index_gh_pages_js=url.get_url('index_gh_pages_js', source),
            data=json_data,
            version=__version__,
            web_version=False)
        
        self.set_header("Content-Type", "text/html")
        self.serve(data)
  
class ProjectHandler(BaseHandler):
    @asynchronous
    @gen.coroutine
    @authenticated
    def get(self, path_I):
        # local variables, objects, and settings
        #source = 'web'
        source = 'local'
        url = urls();
        # parse the path
        path = path_I.replace('.html','');
        # parse the input
        visualization_kwargs = {};
        arguments = [];
        for arg in ['project_id','analysis_id','data_export_id']:
            args = self.get_arguments(arg);
            if len(args)==1:
                visualization_kwargs[arg] = args[0];
                arguments.append(args[0]);
        # get the data to visualize
        if 'analysis_id' in visualization_kwargs and 'data_export_id' in visualization_kwargs:
            #visualization data
            data_json = '';
            data_json = self.get_datajson_analysis(visualization_kwargs['analysis_id'],visualization_kwargs['data_export_id']);
            # make the title name
            titlename = ' '.join([visualization_kwargs['analysis_id']]);
        elif 'project_id' in visualization_kwargs:
            #landing page data
            data_json = '';
            data_json = self.get_datajson_project(visualization_kwargs['project_id']);
            # make the title name
            titlename = ' '.join([visualization_kwargs['project_id']]);
        else:
            # re-direct to 404 page
            print('bad GET');
        # get the template directory
        template_dir = 'container' + '.html';
        # render the template
        template = env.get_template(template_dir)
        data = template.render(d3=url.get_url('d3', source),
                               colorbrewer=url.get_url('colorbrewer', source),
                               jquery=url.get_url('jquery', 'web'),
                               boot_js=url.get_url('boot_js', 'web'),
                               escher_css=url.get_url('escher_css', source),
                               escher_js=url.get_url('escher_js', source),
                               container_js=url.get_url('container_js', source),
                               title_header=titlename,
                               title=titlename,
                               ddt_data=data_json,
                               version=__version__,
                               web_version=False,
                            github=url.get_url('github'),
                            #index_gh_pages_js=url.get_url('index_gh_pages_js', source),
                               vkbeautify=url.get_url('vkbeautify', source))
        
        self.set_header("Content-Type", "text/html")
        self.serve(data)

    def get_datajson_analysis(self,analysis_id_I,table_id_I):
        '''get the json data for the analysis_id from the table_id'''
        data_json_O = '';
        if table_id_I=='export_dataStage01AleTrajectories_js':
            io = stage01_ale_io(session);
            data_json_O = io.export_dataStage01AleTrajectories_js(analysis_id_I,data_dir_I='data_json');
        elif table_id_I=='export_dataStage01PhysiologyRatesAverages_js':
            io = stage01_physiology_io(session);
            data_json_O = io.export_dataStage01PhysiologyRatesAverages_js(analysis_id_I,data_dir_I='data_json');
        elif table_id_I=='export_dataStage01ResequencingHeatmap_js':
            io = stage01_resequencing_io(session);
            data_json_O = io.export_dataStage01ResequencingHeatmap_js(analysis_id_I,data_dir_I='data_json');
        elif table_id_I=='export_dataStage01ResequencingLineage_js':
            io = stage01_resequencing_io(session);
            data_json_O = io.export_dataStage01ResequencingLineage_js(analysis_id_I,data_dir_I='data_json');
        elif table_id_I=='export_dataStage01ResequencingMutationsAnnotatedLineage_js':
            io = stage01_resequencing_io(session);
            data_json_O = io.export_dataStage01ResequencingMutationsAnnotatedLineage_js(analysis_id_I,data_dir_I='data_json');
        elif table_id_I=='export_dataStage01ResequencingMutationsAnnotated_js':
            io = stage01_resequencing_io(session);
            data_json_O = io.export_dataStage01ResequencingMutationsAnnotated_js(analysis_id_I,data_dir_I='data_json');
        elif table_id_I=='export_dataStage01ResequencingCoverage_js':
            io = stage01_resequencing_io(session);
            data_json_O = io.export_dataStage01ResequencingCoverage_js(analysis_id_I,data_dir_I='data_json');
        elif table_id_I=='export_dataStage01ResequencingAmplifications_js':
            io = stage01_resequencing_io(session);
            data_json_O = io.export_dataStage01ResequencingAmplifications_js(analysis_id_I,data_dir_I='data_json');
        elif table_id_I=='export_dataStage02ResequencingHeatmap_js':
            io = stage02_resequencing_io(session);
            data_json_O = io.export_dataStage01ResequencingMutationsAnnotated_js(analysis_id_I,data_dir_I='data_json');
        elif table_id_I=='export_dataStage02IsotopomerFittedNetFluxes_js':
            io = stage02_isotopomer_io(session);
            data_json_O = io.export_dataStage02IsotopomerFittedNetFluxes_js(analysis_id_I,data_dir_I='data_json');
        elif table_id_I=='export_dataStage02IsotopomerFluxMap_js':
            io = stage02_isotopomer_io(session);
            data_json_O = io.export_dataStage02IsotopomerFluxMap_js(analysis_id_I,data_dir_I='data_json');
        elif table_id_I=='export_dataStage02IsotopomerFittedNetFluxDifferences_js':
            io = stage02_isotopomer_io(session);
            data_json_O = io.export_dataStage02IsotopomerFittedNetFluxDifferences_js(analysis_id_I,data_dir_I='data_json');
        elif table_id_I=='export_dataStage02QuantificationPairWiseTest_js':
            io = stage02_quantification_io(session);
            data_json_O = io.export_dataStage02QuantificationPairWiseTest_js(analysis_id_I,data_dir_I='data_json');
        elif table_id_I=='export_dataStage02QuantificationDescriptiveStats_js':
            io = stage02_quantification_io(session);
            data_json_O = io.export_dataStage02QuantificationDescriptiveStats_js(analysis_id_I,data_dir_I='data_json');
        elif table_id_I=='export_dataStage02QuantificationHeatmap_js':
            io = stage02_quantification_io(session);
            data_json_O = io.export_dataStage02QuantificationHeatmap_js(analysis_id_I,data_dir_I='data_json');
        elif table_id_I=='export_dataStage02QuantificationPca_js':
            io = stage02_quantification_io(session);
            data_json_O = io.export_dataStage02QuantificationPca_js(analysis_id_I,data_dir_I='data_json');
        elif table_id_I=='export_dataStage01RNASequencingHeatmap_js':
            io = stage01_rnasequencing_io(session);
            data_json_O = io.export_dataStage01RNASequencingHeatmap_js(analysis_id_I,data_dir_I='data_json');
        elif table_id_I=='export_dataStage01RNASequencingGeneExpDiff_js':
            io = stage01_rnasequencing_io(session);
            data_json_O = io.export_dataStage01RNASequencingGeneExpDiff_js(analysis_id_I,data_dir_I='data_json');
        elif table_id_I=='export_dataStage01RNASequencingGenesFpkmTracking_js':
            io = stage01_rnasequencing_io(session);
            data_json_O = io.export_dataStage01RNASequencingGenesFpkmTracking_js(analysis_id_I,data_dir_I='data_json');
        elif table_id_I=='':
            io = stage02_quantification_io(session);
            data_json_O = io.export_dataStage01PhysiologyRatesAverages_js(analysis_id_I,data_dir_I='data_json');
        else:
            #re-direct to 404
            print('table not found')
        return data_json_O;

    def get_datajson_project(self,project_id_I):
        '''get the json data for the project'''
        data_json_O = '';
        io = visualization_io(session);
        data_json_O = io.export_visualizationProject_js(project_id_I,data_dir_I='data_json');
        return data_json_O;
  
class ContainerHandler(BaseHandler):
    @asynchronous
    @gen.coroutine
    @authenticated
    def get(self, path_I):
        # local variables, objects, and settings
        #source = 'web'
        source = 'local'
        url = urls();
        # parse the path
        path = path_I.replace('.html','');
        # make the title name
        titlename = 'Data-driven tiles';
        # build up the data directory
        data_dir = 'tmp';
        try:
            with open(sbaas_settings.visualization_data+'/'+url.get_url(data_dir, source='local',protocol='https')+'ddt_data.js', "rb") as file:
                ddt_data_js = file.read();
        except:
            ddt_data_js = '';
        # get the template directory
        template_dir = 'container' + '.html';
        # render the template
        template = env.get_template(template_dir)
        data = template.render(d3=url.get_url('d3', source),
            colorbrewer=url.get_url('colorbrewer', source),
            jquery=url.get_url('jquery', source),
            boot_js=url.get_url('boot_js', source),
            boot_css=url.get_url('boot_css', source),
            vkbeautify=url.get_url('vkbeautify', source),
            ddt=url.get_url('ddt', source),
            ddt_data=ddt_data_js,
            title_header=titlename,
            title=titlename,
            version=__version__,
            web_version=False,
            github=url.get_url('github')
            #index_gh_pages_js=url.get_url('index_gh_pages_js', source),
            #d3_chart2d=url.get_url('d3_chart2d', source),
            #d3_chart2d_boxandwhiskers=url.get_url('d3_chart2d_boxandwhiskers', source),
            #d3_chart2d_heatmap=url.get_url('d3_chart2d_heatmap', source),
            #d3_chart2d_horizontalbars=url.get_url('d3_chart2d_horizontalbars', source),
            #d3_chart2d_line=url.get_url('d3_chart2d_line', source),
            #d3_chart2d_packlayout=url.get_url('d3_chart2d_packlayout', source),
            #d3_chart2d_points=url.get_url('d3_chart2d_points', source),
            #d3_chart2d_treelayout=url.get_url('d3_chart2d_treelayout', source),
            #d3_chart2d_verticalbars=url.get_url('d3_chart2d_verticalbars', source),
            #d3_data=url.get_url('d3_data', source),
            #d3_graph2d=url.get_url('d3_graph2d', source),
            #d3_map2d=url.get_url('d3_map2d', source),
            #d3_svg=url.get_url('d3_svg', source),
            #d3_tile=url.get_url('d3_tile', source)
            )
        
        self.set_header("Content-Type", "text/html")
        self.serve(data)
        
class LibHandler(BaseHandler):
    def get(self, path):
        full_path = join(directory, 'lib', path)
        if os.path.isfile(full_path):
            path = full_path
        else:
            raise HTTPError(404)
        self.serve_path(path)

class StaticHandler(BaseHandler):
    def get(self, path):
        path = join(directory, path)
        print('getting path %s' % path)
        self.serve_path(path)

settings = {"debug": "False",
            "cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            "login_url": "/login"}

application = Application([
    (r".*/lib/(.*)", LibHandler),
    (r".*/(fonts/.*)", LibHandler),
    (r".*/(js/.*)", StaticHandler),
    (r".*/(css/.*)", StaticHandler),
    (r".*/(resources/.*)", StaticHandler),
    (r"/(project.*)", ProjectHandler), #refactoring in progress...
    (r"/(container.*)", ContainerHandler), #refactoring in progress...
    (r"/", IndexHandler),
    (r"/login", LoginHandler),
    (r"/logout", LogoutHandler),
], **settings)
 
if __name__ == "__main__":
    # define port
    define("port", default=PORT, type=int, help="Port to serve on.")
    define("public", default=PUBLIC, type=bool,
           help=("If False, listen only on localhost. If True, listen on "
                 "all available addresses."))
    parse_command_line()
    run(port=options.port, public=options.public)
