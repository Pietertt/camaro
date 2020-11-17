<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

use \App\Models\User;

class TestController extends Controller {

    public function test(Request $request){
        $username = $request->input('username');
        $password = $request->input('password');

        $user = User::where('username', $username)->where('password', $password)->get();
        
        if(count($user) == 1){
            return response("Success", 200);
        } else {
            return response("Failure", 403);
        }
    }
    
}
