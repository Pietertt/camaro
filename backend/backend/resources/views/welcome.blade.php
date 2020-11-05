<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="csrf-token" content="{{ csrf_token() }}">

        <!-- UIKit CSS library -->
        <link rel="stylesheet" href="css/uikit.min.css" />
        <script src="js/uikit.min.js"></script>
        <script src="js/uikit-icons.min.js"></script>

        <title>Laravel</title>
    </head>
    <body>
        <div id="app">
            <main-component></main-component>
        </div>
    
        <script type="text/javascript" src="js/app.js"></script>
    </body>
</html>
