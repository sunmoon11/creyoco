require.config({
    baseUrl: '/static/scripts/',
    paths: {
        "eventEmitter": "bower_components/eventEmitter",
        "eventie": "bower_components/eventie",
        "chosen": "thirdparty/chosen.jquery",
        "imagesloaded": "//cdnjs.cloudflare.com/ajax/libs/jquery.imagesloaded/3.0.4/jquery.imagesloaded.min",
        "jquery-pjax": "bower_components/jquery-pjax/jquery.pjax",
        "jquery-cookie": "bower_components/jquery.cookie/jquery.cookie",
        "jquery": "bower_components/jquery/jquery",
        "qtip2": "//cdnjs.cloudflare.com/ajax/libs/qtip2/2.1.1/jquery.qtip.min",
        "jquery-jsonrpc": "thirdparty/jquery.jsonrpc",
        "jquery-form": "bower_components/jquery-form/jquery.form",
        "jstree": "bower_components/jstree-dist/jquery.jstree"
    },

    shim: {
        "jquery-jsonrpc": {
            "deps": ['jquery'],
            "exports": "jQuery.fn.jsonrpc"
        },
        "jquery-cookie": {
            "deps": ['jquery'],
            "exports": "jQuery.fn.cookie"
        },
        "jquery-pjax": {
            "deps": ['jquery']
        },
        "jquery-form": {
            "deps": ['jquery'],
            "exports": "jQuery.fn.form"
        },
        "jstree": {
            "deps": ['jquery'],
            "exports": "jQuery.fn.jstree"
        },
        "chosen": {
            "deps": ['jquery'],
            "exports": "jQuery.fn.chosen"
        }

    },

    packages: [
        {
            name: 'cs',
            location: 'bower_components/require-cs',
            main: 'cs'
        },
        {
            name: "coffee-script",
            location: 'bower_components/coffee-script',
            main: 'index'
        }
    ]
});

require(["mainpage"]);