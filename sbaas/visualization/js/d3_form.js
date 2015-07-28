"use strict";
//var d3_form = function () {
function d3_form() {
    // generic form element
    d3_html.call(this);
    // form specific properties
    this.id = '';
    this.tileid = '';
    this.formelement = null;
    this.form = null;
    this.data = null;
    this.datakeymap = {}; // mapping of keys to data element, chart elements, or other descriptor
};
d3_form.prototype = Object.create(d3_html.prototype);
d3_form.prototype.constructor = d3_form;
d3_form.prototype.add_form2tile = function(){
    // set the form
    var id = this.id;
    var tileid = this.tileid;
    var formclass = this.formclass;
    var listdatafiltered = this.data.listdatafiltered;

    this.formelement = d3.select('#'+tileid+"panel-body").selectAll(".form-responsive")
        .data([listdatafiltered]);
        //.data([0]);

    this.formenter = this.form.enter()
        .append("div")
        .attr("class","form-responsive")
        .append("form")
        .attr("class",formclass)
        .attr("id",id+"form");

    this.form = this.formelement.select("form")
    this.form.exit().remove();

};
d3_form.prototype.set_formclass = function(formclass_I){
    // set the formid
    this.formclass = formclass_I;
};
d3_form.prototype.set_id = function(formid_I){
    // set the formid
    this.id = formid_I;
};
d3_form.prototype.set_tileid = function(formtileid_I){
    // set the form tileid
    this.tileid = formtileid_I;
};
d3_form.prototype.add_data = function(data_I){
    // add data to tile
    this.data = data_I[0];
};
d3_form.prototype.set_datakeymap = function(datakeymap_I){
    // set form data key map
    this.datakeymap = datakeymap_I[0];  
};
d3_form.prototype.add_ndata = function(data_I){
    // add data to tile
    this.data = data_I;
};
d3_form.prototype.set_ndatakeymap = function(datakeymap_I){
    // set form data key map
    this.datakeymap = datakeymap_I;  
};
d3_form.prototype.set_formstyle = function () {
    // predefined css style for form header rows
    var formselector = "#" + this.tileid + " .form-responsive";
    var formstyle = {
        //'form-layout': 'fixed',
        'width': '100%',
        'margin-bottom': '15px',
        'overflow-y': 'scroll',
        //'overflow-y': 'hidden',
        'overflow-x': 'scroll',
        '-ms-overflow-style': '-ms-autohiding-scrollbar',
        //'border': '1px solid #ddd',
        '-webkit-overflow-scrolling': 'touch'
    };
    var selectorstyle = [{ 'selection': formselector, 'style': formstyle }]
    this.set_d3css(selectorstyle);
};
d3_form.prototype.set_d3css = function (selectionstyle_I) {
    //set custom css style to d3
    //Input:
    // selectionstyle_I = [{selection: string e.g., '.axis line, .axis path'
    //                      style: key:value strings e.g., {'fill': 'none', 'stroke': '#000',
    //                                                      'shape-rendering': 'crispEdges'}}]
    for (var i = 0; i < selectionstyle_I.length; i++) {
        d3.selectAll(selectionstyle_I[i].selection)
            .style(selectionstyle_I[i].style);
    };
};
d3_form.prototype.add_draganddrop2form = function () {
    // add file drag and drop for input
};
d3_form.prototype.add_checkbox2form = function () {
    // add checkbox for input
};
d3_form.prototype.add_color2form = function () {
    // add color pallet for input
};
d3_form.prototype.add_range2form = function () {
    // add range slider for input
};
d3_form.prototype.add_form = function(textarea_valuetext_I){
    // add form to tile
    if (typeof texarea_valuetext_I !== "undefined"){var textarea_valuetext = textarea_valuetext_I;}
    else{var textarea_valuetext = this.data.listdatafiltered;}
    var id = this.id;

    this.formform = this.form.selectAll("form")
        .data([textarea_valuetext]);

    this.formformenter = this.formform.enter()
        .append("form")
        .attr("id", id + 'form');

    this.formform.exit().remove();

};
d3_form.prototype.add_input2form = function (textarea_valuetext_I) {
    // add text area for input
    // INPUT:
    if (typeof texarea_valuetext_I !== "undefined"){var textarea_valuetext = textarea_valuetext_I;}
    else{var textarea_valuetext = this.data.convert_filter2stringmenuinput();};

    var id = this.id;

//     this.formform = this.form.append("div")
//         .attr("class","form-group")
//         .attr("id", id + 'form');

//     for (i=0;i<textarea_valuetext.length;i++){
//         var formlabel = this.formform.append("label")
//             .text(textarea_valuetext[i].text)
//             .attr("id", id + 'formlabel' + textarea_valuetext[i].text);
//         var forminput = this.formform.append("input")
//             .attr("class","form-control")
//             .attr("type","text")
//             .attr("placeholder",textarea_valuetext[i].value)
//             .attr("value",textarea_valuetext[i].value)
//             .attr("id", id + 'forminput'+ textarea_valuetext[i].text);
//     };

    this.formformgroup = this.formform.selectAll(".form-group")
        .data(textarea_valuetext);

    this.formformgroupenter = this.formformgroup.enter()
        .append("div")
        .attr("class","form-group")
        .attr("id", id + 'form-group');

    this.formformgroup.exit().remove();

    this.formformlabel = this.formformgroup.selectAll("label")
        .data(function(row){
            var textvalue = [];
            textvalue.push({text:row.text,value:row.value});
            return textvalue;
        });

    this.formformlabelenter = this.formformlabel.enter()
        .append("label")
        .attr("id", function(d){return id + 'formlabel' + d.text;})
        .text(function(d){return d.text;});

    this.formformlabel.transition()
        .attr("id", function(d){return id + 'formlabel' + d.text;})
        .text(function(d){return d.text;});

    this.formformlabel.exit().remove();

    this.formforminput = this.formformgroup.selectAll("input")
        .data(function(row){
            var textvalue = [];
            textvalue.push({text:row.text,value:row.value});
            return textvalue;
        });

    this.formforminput.exit().remove();

    this.formforminput.transition()
        .attr("class","form-control")
        .attr("type","text")
        .attr("value",function(d){return d.value;})
        .attr("id", function(d){return id + 'forminput' + d.text;});

    this.formforminputenter = this.formforminput.enter()
        .append("input")
        .attr("class","form-control")
        .attr("type","text")
        //.attr("placeholder",textarea_valuetext[i].value)
        .attr("value",function(d){return d.value;})
        .attr("id", function(d){return id + 'forminput' + d.text;});
};
d3_form.prototype.update_forminput = function(textarea_valuetext_I){
    // update the form
    if (typeof texarea_valuetext_I !== "undefined"){var textarea_valuetext = textarea_valuetext_I;}
    else{var textarea_valuetext = this.data.convert_filter2stringmenuinput();};
    var id = this.id;

    for (i=0;i<textarea_valuetext.length;i++){
        d3.select("#"+id + 'forminput'+ textarea_valuetext[i].text).node().value=textarea_valuetext[i].value;
    };
};
d3_form.prototype.add_submitbutton2form = function (button_idtext_I) {
    // add submit button
    // INPUT:
    //e.g. {'id':'submit1','text':'submit'};
    if (!button_idtext_I){var button_idtext = {'id':'submit1','text':'submit'};}
    else{var button_idtext = button_idtext_I;}

    var id = this.id;
    var tileid = this.tileid;

    // note: chaining submitbuttongroup to formformenter instead of formform
    // reason:      ensures that buttons will be added only once after a listener event
    //              has been added to the property of the button.
    this.submitbuttongroup = this.formformenter.selectAll(".btn-group")
        .data(button_idtext)

    this.submitbuttongroup.exit().remove();

    this.submitbuttongroupenter = this.submitbuttongroup.enter()
        .append("div")
        .attr("class","btn-group")
        .attr("id", id + "submitbtn-group");

    this.submitbutton = this.submitbuttongroup.selectAll(".btn btn-default")
        .data(function(row){
            var idtext = [];
            idtext.push({id:row.id,text:row.text});
            return idtext;
        });

    this.submitbutton.exit().remove();

    this.submitbutton.transition()
        .attr("type","submit")
        .attr("class", "btn btn-default")
        .attr("id", function(d){return id + 'submitbutton' + d.id;})
        .text(function(d){return d.text;});

    this.submitbuttonenter = this.submitbutton.enter()
        .append("button")
        .attr("type","submit")
        .attr("class", "btn btn-default")
        .attr("id", function(d){return id + 'submitbutton' + d.id;})
        .text(function(d){return d.text;});
};
d3_form.prototype.render = function(){
    // make render function here...
};
d3_form.prototype.add_datalist = function (datalist_valuetext_I) {
    // add datalist (menu) for input
    // INPUT:
    //e.g. [{'value':'hclust','text':'by cluster'},...];

    var tileid = this.tileid;  

    var datalist = this.form.append("select")
        .attr("id", tileid + 'datalist');

    for (var i=0;i<datalist_valuetext_I.length;i++){
        datalist.append("option")
            .attr("value",datalist_valuetext_I[i].value)
            .text(datalist_valuetext_I[i].text);
    };  
};  
d3_form.prototype.set_formsubmitbuttonidtext = function(button_idtext_I) {
    // set submit button
    // INPUT:
    //e.g. {'id':'submit1','text':'submit'};
    if (!button_idtext_I){this.button_idtext = {'id':'submit1','text':'submit'};}
    else{this.button_idtext = button_idtext_I;}
};