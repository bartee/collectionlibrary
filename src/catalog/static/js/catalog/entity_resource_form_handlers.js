var EntityResourceFormcontroller = Class.extend({

    elements:{
        radio_field: false,
        data_field: false,
        url_field: false,
        image_field: false,
        text_field: false
    },

    /**
     * Change the visible fields based on the selected type.
     */
    change: function(){
        this.elements.url_field.val('');
        this.elements.url_field.hide();

        this.elements.image_field.val('');
        this.elements.image_field.hide('');

        this.elements.text_field.val('');
        this.elements.text_field.hide('');

        var type_value = $("input:radio[name ='type']:checked").val();
        if (type_value =='url'){
            this.elements.url_field.show();
        } else if (type_value == 'image') {
            this.elements.image_field.show();
        } else if (type_value == 'text') {
            this.elements.text_field.show();
        } else {
            alert(type_value + ' is not a valid type!');
        }

    },

    init: function(container){
        // Retrieve all containers into pointers
        // set initial score
        this.elements.radio_field = jQuery(container).find('input:radio[name =\'type\']:radio');
        this.elements.data_field = jQuery(container).find('#id_data').parents('.form-row.field-data');
        this.elements.url_field = jQuery(container).find('#id_url').parents('.form-row.field-url');
        this.elements.image_field = jQuery(container).find('#id_image').parents('.form-row.field-image');
        this.elements.text_field = jQuery(container).find('#id_text').parents('.form-row.field-text');
        this.elements.data_field.hide();
        this.elements.radio_field.change(this.change());
        this.change();
    },

})
var erf_controller;
(function($) {
    erf_controller = new EntityResourceFormcontroller('#entityresource_form');
    $('#entityresource_form').find('input:radio[name="type"]:radio').change(function(){
        erf_controller.change();
    });
})(django.jQuery);

