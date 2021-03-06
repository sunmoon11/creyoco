define(['jquery', 'common', 'chosen', 'qtip2', 'jquery-modal'], function($, common) {
    var exports = {
        show_lightbox: function(width, height, el) {            
            el.height(height);
            el.width(width);
            el.modal();                        
        },

        init: function() {
            $(document).ready(function() {
            $(document).on('click', '#navi li a', function(e){
                e.preventDefault();
                history.pushState({page: this.href}, '', this.href);
            });
            $(window).on('popstate', function(e){
              //  loadPage('#frontPage', location.pathname);
                console.log(e.originalEvent.state);
            });
            var url = document.URL;
            if (url.search("export") > 0) {
                $('#middle-row').children().hide();
                $('#properties').show();
                $('#navi li').removeClass('active');
                $('#export').addClass('active');
            }
            if (url.search("edit") > 0) {
                $('#middle-row').children().hide();
                $('#authoring').show();
                $('#navi li').removeClass('active');
                $('#edit').addClass('active');
            }

            if (url.search("layout") > 0) {
                $('#middle-row').children().hide();
                $('#selectStyle').show();
                $('#navi li').removeClass('active');
                $('#layout').addClass('active');
            }

            $('.chzn-select').chosen();
            $('#select_course').change( function() {
                location.href = $(this).val();
            });

            $('#settings_button').qtip ({
                content: 'Hinzufuegen, loeschen oder verschieben der Themen', // Noti ce that content.text is long-hand for simply declaring content as a string

                style: {
                    tip: true,
                    classes: 'tip'
                },

                show: {
                    delay: 500,
                    effect: function(offset) {
                        $(this).slideDown(200); // "this" refers to the tooltip
                    }
                },
                position: {
                adjust: {
                    x: -20
                }
            }
            });

            $('#download_button').qtip ({
                content: 'Formatauswahl und herunterladen des Paketes', // Noti ce that content.text is long-hand for simply declaring content as a string

                style: {
                    tip: true,
                    classes: 'tip'
                },

                show: {
                    delay: 500,
                    effect: function(offset) {
                        $(this).slideDown(200); // "this" refers to the tooltip
                    }
                },
                position: {
                    adjust: {
                        x: -20
                    }
                }
            });

            $('#outline img').click( function() {
                if($(this).attr('id') == 'settings_button') {
                    $(this).removeClass('transparent');
                    $('#download').hide();
                    $('#settings').slideToggle('slow', function() {
                        if($('#settings').is(':visible')) {
                            $(this).removeClass('transparent');
                            $('#download_button').addClass('transparent');
                        }
                        else {
                            $(this).removeClass('transparent');
                            $('#download_button').removeClass('transparent');
                        }
                    });
                }

                else if($(this).attr('id') == 'download_button') {
                    $(this).removeClass('transparent');
                    $('#settings').hide();
                    $('#download').slideToggle('slow', function() {
                        if($('#download').is(':visible')) {
                            $(this).removeClass('transparent');
                            $('#settings_button').addClass('transparent');
                        }
                        else {
                            $(this).removeClass('transparent');
                            $('#settings_button').removeClass('transparent');
                        }
                    });

                }
            });

            $(document).keyup(function(e) {
                if (e.keyCode == 27) {
                    $('#lightbox').hide();
                    $('body').css('overflow', 'auto');
                }
            });

            $('#edit').click( function(){
                $('#middle-row').children().hide();
                $('#authoring').show();
                $('#navi li').removeClass('active');
                $(this).addClass('active');
            });

            $('#layout').click( function(){
                    $('#middle-row').children().hide();
                    $('#selectStyle').show();
                    $('#navi li').removeClass('active');
                    $(this).addClass('active');
            });

            $('#export').click( function(){
                    $('#middle-row').children().hide();
                    $('#properties').show();
                    $('#navi li').removeClass('active');
                    $(this).addClass('active');
            });

            $('#download').click( function () {
                exports.show_lightbox(365, 200, $("#download_box"));
            });
            });
        }
    };
    return exports;
});
