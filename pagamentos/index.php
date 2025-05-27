<?php

$request_uri = $_SERVER['REQUEST_URI'];

if ($request_uri === '/pagamento') {
    $pedidoJson = file_get_contents('http://pedidos:3002/pedido');
    $pedidoData = json_decode($pedidoJson, true);

    $response = [
        'status' => 'paid',
        'pedido' => $pedidoData
    ];

    header('Content-Type: application/json');
    echo json_encode($response);
} else {
    http_response_code(404);
    echo json_encode(['error' => 'Not found']);
}
