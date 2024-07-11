<?php
require_once 'database.php';
require_once 'Tokoroti.php';

$db = new MySQLDatabase();
$tokoroti = new Tokoroti($db);
$id=0;
$kd_produk=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];

// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kd_produk'])){
            $kd_produk = $_GET['kd_produk'];
        }
        
        if($id>0){    
            $result = $tokoroti->get_by_id($id);
        }elseif($kd_produk>0){
            $result = $tokoroti->get_by_kd_produk($kd_produk);
        } else {
            $result = $tokoroti->get_all();
        }        
       
        $roti = array();
        while ($row = $result->fetch_assoc()) {
            $roti[] = $row;
        }
        header('Content-Type: application/json');
        echo json_encode($roti);
        break;

    case 'POST':
        // Add a new mahasiswa
        $tokoroti->kd_produk = $_POST['kd_produk'];
        $tokoroti->nama = $_POST['nama'];
        $tokoroti->stok = $_POST['stok'];
        $tokoroti->insert();
        
        $a = $db->affected_rows();

        if($a>0){
            $data['status']='success';
            $data['message']='Data created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data not created.';
        }
        header('Content-Type: application/json');
        echo json_encode($data);
        break;

    case 'PUT':
        // Update an existing mahasiswa
        $_PUT = [];
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kd_produk'])){
            $kd_produk = $_GET['kd_produk'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $tokoroti->kd_produk = $_PUT['kd_produk'];
        $tokoroti->nama = $_PUT['nama'];
        $tokoroti->stok = $_PUT['stok'];
        if($id>0){    
            $tokoroti->update($id);
        }elseif($kd_produk>0){
            $tokoroti->update_by_kd_produk($kd_produk);
        } else {
            
        } 
        
        $a = $db->affected_rows();

        if($a>0){
            $data['status']='success';
            $data['message']='Data updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;

    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kd_produk'])){
            $kd_produk = $_GET['kd_produk'];
        }
        if($id>0){    
            $tokoroti->delete($id);
        }elseif($kd_produk>0){
            $tokoroti->delete_by_kd_produk($kd_produk);
        } else {
            
        } 
        
        $a = $db->affected_rows();

        if($a>0){
            $data['status']='success';
            $data['message']='Data deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data delete failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;

    default:
        header("HTTP/1.0 405 Method Not Allowed");
        break;
}
$db->close()
?>
