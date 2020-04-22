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

function acionamento_manual(){
    var switchState = ($("input['name'='switch.auto']").is(":checked"))? true : false
}