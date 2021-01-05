<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

use \App\Models\User;
use \App\Models\JWT;

class AuthenticationController extends Controller {

    public function verify_user(Request $request){
        $username = $request->input('username');
        $password = $request->input('password');

        $user = User::where('username', $username)->where('password', $password)->first();
        
        if($user !== null){
            $jwt = new JWT();
            $user->token = $jwt->get_token();
            $user->save();
            return response(json_encode($user), 200);
        } else {
            
            return response("Error", 403);
        }
    }

    public function create_user(Request $request){
        $username = $request->input('username');
        $email = $request->input('email');
        $password = $request->input('password');

        if(empty($username)) return response("Error", 403);
        if(empty($email)) return response("Error", 403);
        if(empty($password)) return response("Error", 403);

        $user = new User;
        $user->username = $username;
        $user->email = $email;
        $user->token = "";
        $user->password = $password;
        $user->save();

        return response("Success", 200);
    }

    public function verify_token(Request $request){
        $id = $request->input('id');

        $user = User::where('id', $id)->first();

        return response(json_encode($user->token), 200);
    }
    
}
