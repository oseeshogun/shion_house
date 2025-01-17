$(document).ready(function(){
    
    (function($) {
        "use strict";

    
    jQuery.validator.addMethod('answercheck', function (value, element) {
        return this.optional(element) || /^\bcat\b$/.test(value)
    }, "Veuillez entrer la bonne réponse");

    // validate contactForm form
    $(function() {
        $('#contactForm').validate({
            rules: {
                name: {
                    required: true,
                    minlength: 2
                },
                subject: {
                    required: true,
                    minlength: 4
                },
                number: {
                    required: true,
                    minlength: 5
                },
                email: {
                    required: true,
                    email: true
                },
                message: {
                    required: true,
                    minlength: 20
                }
            },
            messages: {
                name: {
                    required: "Veuillez entrer votre nom",
                    minlength: "Votre nom doit contenir au moins 2 caractères"
                },
                subject: {
                    required: "Veuillez entrer un sujet",
                    minlength: "Le sujet doit contenir au moins 4 caractères"
                },
                number: {
                    required: "Veuillez entrer votre numéro",
                    minlength: "Votre numéro doit contenir au moins 5 caractères"
                },
                email: {
                    required: "L'adresse email est requise",
                    email: "Veuillez entrer une adresse email valide"
                },
                message: {
                    required: "Veuillez entrer votre message",
                    minlength: "Votre message doit contenir au moins 20 caractères"
                }
            },
            submitHandler: function(form) {
                $(form).ajaxSubmit({
                    type:"POST",
                    data: $(form).serialize(),
                    url: "/contact/message",
                    success: function() {
                        $('#contactForm :input').attr('disabled', 'disabled');
                        $('#contactForm').fadeTo( "slow", 1, function() {
                            $(this).find(':input').attr('disabled', 'disabled');
                            $(this).find('label').css('cursor','default');
                            $('#success').fadeIn()
                            $('.modal').modal('hide');
		                	$('#success').modal('show');
                        })
                    },
                    error: function() {
                        $('#contactForm').fadeTo( "slow", 1, function() {
                            $('#error').fadeIn()
                            $('.modal').modal('hide');
		                	$('#error').modal('show');
                        })
                    }
                })
            }
        })
    })
        
 })(jQuery)
})