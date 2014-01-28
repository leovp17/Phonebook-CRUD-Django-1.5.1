$(document).ready(function(){

    //Se agrega funcionalidad a btn para insertar formulario en la pagina /recipe/

    $(".add-recipe2").click(function(e) { // for each edit contact url
        e.preventDefault(); // prevent navigation
        var url = $(this).data("form"); // get the contact form url
        $("#recipeForm").load(url);
        return false; // prevent the click propagation
    });

    // Al hacer submit en el formulario, se envian los datos via ajax, seguidamente se elimina el formulario de la pagina y se refresca a lista de recetas.
    $("#recipeForm").on('submit', 'form', function() {
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
                    $("#recipeForm").html(data.data);

                }
                else if (data.status=="ok"){
                    console.log("datos receta correctos")

                    $("#recipeformulario").remove();

                    reloadRecipes()

                    console.log(data.data);

                }
                return false;

            },

            error: function() { // on error..
            console.log("cueck receta submit");


            }
        });
        return false;
    });

    function reloadRecipes(){

            var urlContacts = $(location).attr('href'); // get the contact list url

            $("#recetas").load("/recipes/ #recetas .receta");

        };


});