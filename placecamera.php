<?php
$extra_path = str_replace($_SERVER['SCRIPT_NAME'],'',$_SERVER['REQUEST_URI']);
$parts = explode('/',$extra_path);

$my_img = imagecreate( $parts[1], $parts[2] );
$background = imagecolorallocate( $my_img, 128, 128, 128 );
$text_colour = imagecolorallocate( $my_img, 55, 55, 55 );
$text = 'Testing..';

$font = 'Monaco_Linux.ttf';

imagettftext($my_img, 20, 0, 100, 200, $text_colour, $font, $text);

header( "Content-type: image/png" );
imagepng( $my_img );
imagecolordeallocate( $text_color );
imagecolordeallocate( $background );
imagedestroy( $my_img );
?>
