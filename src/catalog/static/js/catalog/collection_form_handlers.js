var date_diff_indays = function(date1, date2) {
    dt1 = new Date(date1);
    dt2 = new Date(date2);
    num_days = Math.floor(
        (
            Date.UTC(dt2.getFullYear(), dt2.getMonth(), dt2.getDate()) -
            Date.UTC(dt1.getFullYear(), dt1.getMonth(), dt1.getDate()) )
        /
        (1000 * 60 * 60 * 24));
}

var CollectionFormController = Class.extend({
    elements: {
        start_date_field: false,
        end_date_field: false,
        output: false,
        dummyform_row: false
    },

    selectors: {
        start_date_field: "#id_start_date",
        end_date_field: "#id_end_date",
        output_container: "#output_container",
        relational_form: "#relational_form",
        row_datefield: '[class="datefield"]',
        row_displaydate: '[class="datefield_display"]',
        row_entity: '[class="entity"]',
        row_note: '[class="note"]'
    },

    date_range: [],

    entity_elations: [],

    init: function(container){
        // Retrieve all containers into pointers
        // set initial score
        this.elements.start_date_field = jQuery(container).find(this.selectors.start_date_field);
        this.elements.end_date_field = jQuery(container).find(this.selectors.end_date_field);
        this.elements.output = jQuery(container).find(this.selectors.output_container);
        this.elements.dummyform_row = jQuery(container).find(this.selectors.relational_form);
        this.bind();
    },

    /**
     * Bind listeners to the start- and end date field
     */
    bind: function(){
        this.elements.start_date_field.on('change paste keyup', jQuery.proxy(function(){ this.change(); }, this));
        this.elements.end_date_field.on('change paste keyup', jQuery.proxy(function(){ this.change(); }, this));
    },

    /**
     * Change handler
     */
    change: function(){
        start_date_val = this.elements.start_date_field.val();
        end_date_val = this.elements.end_date_field.val();
        if (start_date_val && end_date_val){
            start_date = new Date(start_date_val);
            end_date = new Date(end_date_val);
            if (start_date > end_date){

                // flip em around
                this.elements.start_date_field.val(end_date_val);
                this.elements.end_date_field.val(start_date_val);
                this.change();
            }
            num_days = Math.floor(
                (
                    Date.UTC(end_date.getFullYear(), end_date.getMonth(), end_date.getDate()) -
                    Date.UTC(start_date.getFullYear(), start_date.getMonth(), start_date.getDate()) )
                /
                (1000 * 60 * 60 * 24));
            this.date_range = [];
            /**
             * - Make date range from difference
             */
            for (index = 0; index < num_days; index ++){
                new_date = new Date(start_date.getFullYear(), start_date.getMonth(), start_date.getDate() + index);
                this.date_range.push(new_date);
            }
            this.render();
        }
    },

    /**
     * Collect the inline form input and put it a list
     */
    collect_form_input: function(){

    },

    /**
     * Here's where the form is rendered.
     *
     * That form is for searching an entity and adding a note. So that's
     * - a hidden field for the date
     * - an autocomplete field, and a text input.
     * Handling will be done in the backend.
     */
    render: function(){
        this.collect_form_input();
        this.elements.output.html();

        for (i in this.date_range){
            new_date = this.date_range[i];
            verbose_date = new_date.getDate() + " " + new_date.getMonth() + " " + new_date.getFullYear();

            new_row = jQuery(this.elements.dummyform_row.clone());

            new_row.attr('id','');
            new_row.find(this.selectors.row_datefield).val(new_date);
            new_row.find(this.selectors.row_displaydate).html(verbose_date );

            new_row.find(this.selectors.row_entity).materialize_autocomplete({
                limit: 20,
                getData: function (text, callback) {
                    $.ajax({
                        url: 'http://127.0.0.1:8000/catalog/entity_autocomplete/',
                        data :{
                            q: text
                        },
                    }).done(jQuery.proxy(function(data){
                        resultset = data.results;
                        callback(text, resultset);
                    }, callback));
                },
                dropdown: {
                    className: 'dropdown-content ac-dropdown'
                },
                minLength: 3
            });

            new_row.removeClass('hide');
            this.elements.output.append(new_row);
        }

    }
});

var cf_controller = new CollectionFormController('#collection_form');
jQuery('.datepicker').pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 3, // Creates a dropdown of 15 years to control year,
    today: 'Today',
    clear: 'Clear',
    close: 'Ok',
    closeOnSelect: true // Close upon selecting a date,
});



