<?php

namespace App\Models;


class JWT {
    private $token;

    function __construct(){
        $token = bin2hex(random_bytes(200));
        $this->token = $token;
    }

    public function get_token(){
        return $this->token;
    }
}
