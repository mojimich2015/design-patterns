<?php

class Proxy {
    public $obj;

    public function __construct($obj){
        $this->obj = $obj;
    }

    public function __call($method, $parameters){
        return $this->obj->{$method}{... $parameters}
    }
}
?>

Example usage in Laravel: tap builtin helper function