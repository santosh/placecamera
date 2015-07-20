<?php
$extra_path = str_replace($_SERVER['SCRIPT_NAME'],'',$_SERVER['REQUEST_URI']);
$parts = explode('/',$extra_path);

$width = $parts[1];
$height = $parts[2];

$my_img = imagecreate( $width, $height );
$background = imagecolorallocate( $my_img, 128, 128, 128 );
$text_colour = imagecolorallocate( $my_img, 55, 55, 55 );
$text = $height . ' x ' . $width;

$font = 'Monaco_Linux.ttf';

imagettftext($my_img, 20, 0, $width/2-70, $height/2, $text_colour, $font, $text);

header( "Content-type: image/png" );
imagepng( $my_img );
imagecolordeallocate( $text_color );
imagecolordeallocate( $background );
imagedestroy( $my_img );
?>
