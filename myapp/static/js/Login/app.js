// make console.log safe to use
window.console||(console={log:function(){}});

$(document).ready(function() {

    $("#SSherkat").click(function () {
        $("#Btns").addClass('hidden').removeClass('show');
        $("#Ssbt").removeClass('hidden').addClass('show');
    })


    $("#Bazgasht1").click(function () {
        $("#Btns").addClass('show').removeClass('hidden');
        $("#Ssbt").removeClass('show').addClass('hidden');
    })


    $("#SKarbar").click(function () {
        $("#Btns").addClass('hidden').removeClass('show');
        $("#Ksbt").removeClass('hidden').addClass('show');
    })


    $("#Bazgasht2").click(function () {
        $("#Btns").addClass('show').removeClass('hidden');
        $("#Ksbt").removeClass('show').addClass('hidden');
    })
    //Init the genyxAdmin plugin

    //Disable certain links
    $('a[href^=#]').click(function (e) {
        e.preventDefault()
    })

    //------------- Prettify code  -------------//
    window.prettyPrint && prettyPrint();

    //------------- Bootstrap tooltips -------------//
    $("[data-toggle=tooltip]").tooltip ({});
    $(".tip").tooltip ({placement: 'top', container: 'body'});
    $(".tipR").tooltip ({placement: 'right', container: 'body'});
    $(".tipB").tooltip ({placement: 'bottom', container: 'body'});
    $(".tipL").tooltip ({placement: 'left', container: 'body'});
    //--------------- Popovers ------------------//
    //using data-placement trigger
    $("a[data-toggle=popover]")
      .popover()
      .click(function(e) {
        e.preventDefault()
    });

    $('#fixedwidth').click(function() {
        $.genyxAdmin({fixedWidth: true});
    });

    //init this last don`t change
    //------------- Uniform  -------------//
    //add class .nostyle if not want uniform to style field
    //$("input, textarea, select").not('.nostyle').uniform();
    $("[type='checkbox'], [type='radio'], [type='file'], select").not('.toggle, .select2, .multiselect').uniform();
});

