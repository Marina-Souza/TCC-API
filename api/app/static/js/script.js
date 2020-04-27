function request_url(idDispositivo) {
    $.ajax({
        method: 'GET',
        url: '/manual/' + idDispositivo + '/1'
    }).done(function( msg ) {
        $('[data-id=' + idDispositivo + ']').text(msg);
        setTimeout(function(){
            $('[data-id=' + idDispositivo + ']').text('');
        }, 3000);
    }).error(function() {
        $('[data-id=' + idDispositivo + ']').text('Falha no envio!');
        setTimeout(function(){
            $('[data-id=' + idDispositivo + ']').text('');
        }, 3000);
    });
}
function atualiza_parametros(param) {
    $('#auto-switch').prop('checked', param=='True');
}

function automatico_condutividade() {
    const switchState = ($("#auto-switch").is(":checked"))? true : false
    const inputValue = $("#auto-input").val()
    const data = {
        condutividade: inputValue,
        ativo: switchState
    }

    $.ajax({
        method: 'GET',
        url: '/condutividade/',
        dataType: 'json',
        data: data
    }).done(function( msg ) {
        alert(msg);
    }).error(function() {
        alert('Erro');
    });
}
function alarme(param) {
    const row = param.parentElement;
    debugger;
    const switchState = $(row).find('.switch > label > input').is(":checked") ? true : false
    const inputValue = $(row).find('.input-field > input').val()
    const alertType = row.dataset.type;
    const data = {
        valor: inputValue,
        ativo: switchState,
        tipo: alertType
    }

    $.ajax({
        method: 'GET',
        url: '/alerta/',
        dataType: 'json',
        data: data
    }).done(function( msg ) {
        //alert(msg);
    }).error(function() {
        //alert('Erro');
    });
}