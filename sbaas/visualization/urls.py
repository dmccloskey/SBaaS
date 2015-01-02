from version import __version__

# TODO remove all os.path.join when using urls

class urls():

    def __init__(self):

        self._visualization_css = {
            #style sheets:
            'barchart_css': 'css/barchart.css',
            'heatmap_css': 'css/heatmap.css',
            'heatmap_expression_css': 'css/heatmap_expression.css',
            'reingoldTilfordTree_css': 'css/reingoldTilfordTree.css',
            'scatterlineplot_css': 'css/scatterlineplot.css',
            'index_css': 'css/index.css',
            'boxandwhiskers_css': 'css/boxandwhiskers.css',
            'scatterplot_css': 'css/scatterplot.css',
            'metabolicmap_css': 'css/metabolicmap.css'
            }

        self._visualization_js = {
            #javascript:
            'barchart_js': 'js/barchart.js',
            'heatmap_js': 'js/heatmap.js',
            'heatmap_hcluster_index_js': 'js/heatmap_hcluster_index.js',
            'heatmap_expression_js': 'js/heatmap_expression.js',
            'reingoldTilfordTree_js': 'js/reingoldTilfordTree.js',
            'scatterlineplot_js': 'js/scatterlineplot.js',
            'utilities_js': 'js/utilities.js',
            'index_js': 'js/index.js',
            'boxandwhiskers_js': 'js/boxandwhiskers.js',
            'boxandwhiskers_ratios_index_js': 'js/boxandwhiskers_ratios_index.js',
            'boxandwhiskers_concentrations_index_js': 'js/boxandwhiskers_concentrations_index.js',
            'scatterplot_js': 'js/scatterplot.js',
            'scatterplot_volcanoplot_index_js': 'js/scatterplot_volcanoplot_index.js',
            'scatterplot_pcaplot_index_js': 'js/scatterplot_pcaplot_index.js',
            'metabolicmap_js': 'js/metabolicmap.js',
            'metabolicmap_thermodynamics_index_js': 'js/metabolicmap_thermodynamics_index.js',
            'metabolicmap_fluxomics_index_js': 'js/metabolicmap_fluxomics_index.js',
            'metabolicmap_sampling_index_js': 'js/metabolicmap_sampling_index.js'
            #TODO:
            #'visualization': 'lib/visualization.%s.js' % __version__,
            #'visualization_min': 'lib/visualization.%s.min.js' % __version__,
            }

        self._visualization_data_dir = {
            #data files:
            'ALEsKOs01/physiology/barchart': 'data/ALEsKOs01/physiology/barchart/',
            'ALEsKOs01/physiology/metabolicmap': 'data/ALEsKOs01/physiology/metabolicmap/',
            'ALEsKOs01/resequencing/heatmap': 'data/ALEsKOs01/resequencing/heatmap/',
            'ALEsKOs01/resequencing/scatterlineplot': 'data/ALEsKOs01/resequencing/scatterlineplot/',
            'ALEsKOs01/ale/scatterlineplot': 'data/ALEsKOs01/ale/scatterlineplot/',
            'ALEsKOs01/resequencing-physiology/heatmap': 'data/ALEsKOs01/resequencing-physiology/heatmap/',
            'ALEsKOs01/isotopomer/metabolicmap':'data/ALEsKOs01/isotopomer/metabolicmap/',
            'genomatica01/quantification/boxandwhiskers':'data/genomatica01/quantification/boxandwhiskers/',
            'ALEWt01/quantification/boxandwhiskers':'data/ALEWt01/quantification/boxandwhiskers/',
            'ALEWt01/quantification/scatterplot':'data/ALEWt01/quantification/scatterplot/',
            'ALEWt01/quantification/metabolicmap':'data/ALEWt01/quantification/metabolicmap/',
            'ALEWt01/quantification/heatmap':'data/ALEWt01/quantification/heatmap/',
            'rpomut01/quantification/boxandwhiskers':'data/rpomut01/quantification/boxandwhiskers/',
            'rpomut01/quantification/scatterplot':'data/rpomut01/quantification/scatterplot/',
            'rpomut01/quantification/heatmap':'data/rpomut01/quantification/heatmap/',
            'rpomut02/quantification/boxandwhiskers':'data/rpomut02/quantification/boxandwhiskers/',
            'rpomut02/quantification/scatterplot':'data/rpomut02/quantification/scatterplot/',
            'rpomut02/quantification/metabolicmap':'data/rpomut02/quantification/metabolicmap/',
            'rpomut02/quantification/heatmap':'data/rpomut02/quantification/heatmap/',
            'chemoNLim01/quantification/boxandwhiskers':'data/chemoNLim01/quantification/boxandwhiskers/',
            'chemoNLim01/quantification/scatterplot':'data/chemoNLim01/quantification/scatterplot/',
            'chemoNLim01/quantification/heatmap':'data/chemoNLim01/quantification/heatmap/',
            'WTEColi113C80U13C2001/isotopomer/metabolicmap':'data/WTEColi113C80U13C2001/isotopomer/metabolicmap/'
            }

        self._resources = {
            #local resources:
            'logo1': 'resources/SBaaS-01.png',
            'logo2': 'resources/SBaaS-02.png',
            'logo3': 'resources/SBaaS-03.png',
            'logo4': 'resources/SBaaS-04.png',
            'logo5': 'resources/SBaaS-05.png',
            'logo6': 'resources/SBaaS-06.png',
            'index_filter': 'resources/index_filter.js'
            }
    
        self._dependencies = {
            'd3': 'lib/d3.min.js',
            'boot_js': 'lib/bootstrap-3.1.1.min.js',
            'boot_css': 'lib/bootstrap-3.1.1.min.css',
            'jquery': 'lib/jquery-2.1.3.min.js',
            'require_js': 'lib/require.min.js',
            'bacon': 'lib/bacon-0.7.12.min.js',
            'vkbeautify':'lib/vkbeautify.0.99.00.beta.js'
            }
    
        self._dependencies_cdn = {
            'd3': '//cdnjs.cloudflare.com/ajax/libs/d3/3.4.8/d3.min.js',
            'boot_js': '//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js',
            'boot_css': '//netdna.bootstrapcdn.com/bootswatch/3.1.1/simplex/bootstrap.min.css',
            'jquery': '//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js',
            'require_js': '//cdnjs.cloudflare.com/ajax/libs/require.js/2.1.11/require.min.js',
            'bacon': '//cdnjs.cloudflare.com/ajax/libs/bacon.js/0.7.12/bacon.min.js',
            'prettify':'//cdnjs.cloudflare.com/ajax/libs/prettify/188.0.0/prettify.js',
            }

        self._links = {
            'github': '//github.com/sbrg/sbaas',
            }
    
        # external dependencies
        self.names = self._visualization_css.keys() + self._visualization_js.keys() + self._visualization_data_dir.keys() + self._resources.keys() + self._dependencies.keys() + self._links.keys()

    def get_url(self, name, source='web', local_host=None, protocol=None):
        """Get a url.

        Arguments
        ---------

        name: The name of the URL. Options are available in urls.names.

        source: Either 'web' or 'local'. Cannot be 'local' for external links.

        protocol: The protocol can be 'http', 'https', or None which indicates a
        'protocol relative URL', as in //zakandrewking.github.io/escher. Ignored if
        source is local.

        local_host: A host url, including the protocol. e.g. http://localhost:7778.

        """
        if source not in ['web', 'local']:
            raise Exception('Bad source: %s' % source)
    
        if protocol not in [None, 'http', 'https']:
            raise Exception('Bad protocol: %s' % protocol)

        if protocol is None:
            protocol = ''
        else:
            protocol = protocol + ':'

        def apply_local_host(url):
            return '/'.join([local_host.rstrip('/'), url])
        
        # visualization_css
        if name in self._visualization_css:
            if source=='local':
                if local_host is not None:
                    return apply_local_host(self._visualization_css[name])
                return self._visualization_css[name]
            return protocol + self._links['github'] + '/visualization/' + self._visualization_css[name]
        # visualization_js
        elif name in self._visualization_js:
            if source=='local':
                if local_host is not None:
                    return apply_local_host(self._visualization_js[name])
                return self._visualization_js[name]
            return protocol + self._links['github'] + '/visualization/' + self._visualization_js[name]
        # visualization_data
        elif name in self._visualization_data_dir:
            if source=='local':
                if local_host is not None:
                    return apply_local_host(self._visualization_data_dir[name])
                return self._visualization_data_dir[name]
            return protocol + self._links['github'] + '/visualization/' + self._visualization_data_dir[name]
        # resources
        elif name in self._resources:
            if source=='local':
                if local_host is not None:
                    return apply_local_host(self._resources[name])
                return self._resources[name]
            return protocol + self._links['github'] + '/visualization/' + self._resources[name]
        # links
        elif name in self._links:
            if source=='local':
                raise Exception('Source cannot be "local" for external links')
            return protocol + self._links[name]
        # local dependencies
        elif name in self._dependencies and source=='local':
            if local_host is not None:
                return apply_local_host(self._dependencies[name])
            return self._dependencies[name]
        # cdn dependencies
        elif name in self._dependencies_cdn and source=='web':
            return protocol + self._dependencies_cdn[name]
        else:
            raise Exception('name not found')

    def data_name_to_url(self, dir, name, protocol='https'):
        """Convert short name to url.

        """
        parts = name.split(':')
        if len(parts) != 2:
            raise Exception('Bad model name')
        longname = name + '.js';
        return '/'.join([get_url(dir, source='web', protocol=protocol), longname])
