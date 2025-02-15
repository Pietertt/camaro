<?php

use \App\Models\User;
use \App\Http\Controllers\ValidationController;

/** @var \Laravel\Lumen\Routing\Router $router */

/*
|--------------------------------------------------------------------------
| Application Routes
|--------------------------------------------------------------------------
|
| Here is where you can register all of the routes for an application.
| It is a breeze. Simply tell Lumen the URIs it should respond to
| and give it the Closure to call when that URI is requested.
|
*/

$router->post('/valid', 'AuthenticationController@verify_user');
$router->post('/valid/token', 'AuthenticationController@verify_token');
$router->post('/create', 'AuthenticationController@create_user');
