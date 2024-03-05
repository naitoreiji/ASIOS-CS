<?php
si ( $ _POST ){
  $firstname = $_POST ['firstname']
  $email = $_POST ['e-mail'] ;
  $name = $_POST ['name'] ;
  $message = $_POST ['message'];
  $headers = " MIME-Version : 1.0\r\n" ;
  $headers .= " content-type : text/plain; charset=iso-8859-1\r\n" ;
  $headers .= " From: $name <$email>\r\n Reply-to : $name <$email > \n X-Mailer:PHP ";
  $subject="$object";
  $destinataire ="ccsc.procassin@gmail.com";
  $body ="$message" ;
  if (mail( $destinataire,$subject,$body,$headers )) {
    $response [ 'status' ] = 'succès' ;
    $response [ 'msg' ] = 'votre mail est envoyé' ;
  } else {
    $response [ 'status' ] = 'erreur' ;
    $response [ 'msg' ] = 'Quelque chose na pas fonctioner' ;
  }

  echo json_encode( $response );
}
?>