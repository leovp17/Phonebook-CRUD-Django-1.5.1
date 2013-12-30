$(document).ready(function(){


        $("#addContact").click(function(e) { // for each edit contact url
            e.preventDefault(); // prevent navigation
            var url = $(this).data("form"); // get the contact form url
            $("#contactForm").load(url);
            return false; // prevent the click propagation
        });

        $('#contactForm').on('submit', 'form', function () {

            //alert(csrftoken);
            $.ajax({
                type: "POST",

                dataType: "json",

                url: $(this).attr('action'),

                data: $(this).serialize(),

                success: function(data, textStatus) { // on success..
                    console.log(data.status);
                    console.log(data.data);
                    if (data.status=="novalido")
                    {
                        console.log("presenta problemas")
                        $("#contactForm").html(data.data);
                    }
                    else if (data.status=="ok")
                    {
                        console.log("bien")
                        $("#contactForm").remove();
                        reloadContacts();
                    }
                    return false;
                },

                error: function() { // on error..
                    console.log("cueck")


                }
            });
            return false;
        });

        function reloadContacts(){

            var urlContacts = $(location).attr('href'); // get the contact list url

            $("#content .table").load("/micrud/ .table .row");

        };



    });