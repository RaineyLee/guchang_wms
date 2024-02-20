<?php
// $conn = mysqli_connect("localhost", "scott", "tiger", "webserver");

// $list = '';
// $sql = "SELECT * FROM topic LIMIT 1000";
// $result = mysqli_query($conn, $sql);

// while($row = mysqli_fetch_array($result)){
//     $list = $list."<li><a href=\"index.php?id={$row['id']}\">{$row['title']}</a></li>";
// }
 
// $article = array(
//     'title' => 'Welcom',
//     'description' => 'Hello WEB.'
// );

// $update_link = '';
// $delete_link = '';
// if(isset($_GET['id'])){
//     // mysqli_real_escape_string() --> secure inputed variable ex) mysqli_real_escape_string({$_GET['id']})
//     $sql = "SELECT * FROM topic WHERE id = {$_GET['id']}";
//     $result = mysqli_query($conn, $sql);
//     $row = mysqli_fetch_array($result);

//     $article['title'] = $row['title'];
//     $article['description'] = $row['description'];
    
//     $update_link = '<a href="update.php?id='.$_GET['id'].'">update</a>';
//     $delete_link = '<a href="delete.php?id='.$_GET['id'].'">delete</a>';
// }
?>

<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>WEB</title>
  </head>
  <body>
  <h1>Success!!!</h1>
    <!--<h1><a href="index.php">WEB</a></h1>-->
    <!--<ol>-->
    <!--    <?=$list?>-->
    <!--</ol>-->
    <!--<a href="create.php">create</a>    -->
    <!--<?=$update_link?>-->
    <!--<?=$delete_link?>-->
    <!--<h2><?=$article['title']?></h2>-->
    <!--<?=$article['description']?>-->
  </body>
</html>