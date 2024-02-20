<?php

if ($_SERVER['REQUEST_METHOD'] == 'POST') {

    include_once("config.php");

    @$id = $_POST['sales_id'];

    // if($id == '' || $name == '' || $code == '')
    // {
    //     echo json_encode(array(
    //         "status" => "false",
    //         "message" => "필수 인자가 부족합니다")
    //     );
    // }
    // else
    // {
    $query= "SELECT item_id, item_name, location, quantity FROM sales_list WHERE order_num = '$id';";
    $result= mysqli_query($con, $query);
    $emparray = array();

    if(mysqli_num_rows($result) > 0)
    {  
        while ($row = mysqli_fetch_assoc($result))
        {
            // $emparray[] = $row;
            echo json_encode(
                ($row
            ), JSON_UNESCAPED_UNICODE
        );

        }

        // echo json_encode(
        //     array(
        //         // "id" => $emparray[0],
        //         // "name" => $emparray[1],
        //         // "code" => $emparray[2]
        //         $emparray
        //     ), JSON_UNESCAPED_UNICODE
        // );
    }
    else
    {
        echo json_encode(
            array(
            "status" => "false",
            "message" => "조회된 정보가 없습니다."
            ), JSON_UNESCAPED_UNICODE
        );
    }

}
else{
    echo json_encode(
        array(
        "status" => "false",
        "message" => "호출방식 에러입니다."
        ), JSON_UNESCAPED_UNICODE
    );
}
        
mysqli_close($con);


?>