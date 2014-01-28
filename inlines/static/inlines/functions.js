
$(document).ready(function () {

    $("#render_education .edit").click(function() {
        submitFormacion();
        $.ajax({
            type: "POST",

            dataType: "json",

            url: "/show_edu/",

            data: {candidato: $("#candidato").val()},

            success: function(data, textStatus) { // on success..
                console.log(data.status);
                console.log(data.data);

                if (data.status=="ok") {
                    $("#render_formeducation").html(data.data);
                    formset_edu();
                }
                else {
                    console.log("datos correctos");
                }
                return false;

            },

            error: function() { // on error..
            console.log("cueck edit button")
            }
        });
        return false;


    });

});

// Show|Hide elements by ID
// User: alexandervolantines
// from candidate_v2.js

function open_id(id) {

    var id="#".concat(id);
    var options = {};

    $(id).show("blind", options, 500);
};

function close_id(id) {
    var id="#".concat(id);
    var options = {};

    $(id).hide("blind", options, 500);
    return false;
};

function submitFormacion(){
    $("#render_formeducation").on('submit', 'form', function() {
        $.ajax({
            type: "POST",

            dataType: "json",

            url: $(this).attr('action'),

            data: $(this).serialize(),

            success: function(data, textStatus) { // on success..
                console.log(data.status);
                console.log(data.data);
                if (data.status=="novalido") {
                    console.log("receta presenta problemas")
                    $("#render_formeducation").html(data.data);

                }
                else if (data.status=="ok"){
                    console.log("datos correctos")

                    $("#render_education_container").html(data.data);

                    $("#formeducation").remove();

                    console.log(data.data);

                    $("#render_history").html(data.historial);


                }
                return false;

            },

            error: function() { // on error..
            console.log("cueck submit");


            }
        });
        return false;
    });
};




