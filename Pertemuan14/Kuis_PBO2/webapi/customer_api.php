<?php
require_once 'database.php';
require_once 'Customer.php';

$db = new MySQLDatabase();
$customer = new Customer($db);
$id=0;
$ktp=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];

// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['ktp'])){
            $ktp = $_GET['ktp'];
        }
        
        if($id>0){    
            $result = $customer->get_by_id($id);
        }elseif($ktp>0){
            $result = $customer->get_by_ktp($ktp);
        } else {
            $result = $customer->get_all();
        }        
       
        $mhs = array();
        while ($row = $result->fetch_assoc()) {
            $mhs[] = $row;
        }
        header('Content-Type: application/json');
        echo json_encode($mhs);
        break;

    case 'POST':
        // Add a new customer
        $customer->ktp = $_POST['ktp'];
        $customer->nama = $_POST['nama'];
        $customer->jk = $_POST['jk'];
        $customer->kota = $_POST['kota'];
        $customer->insert();
        
        $a = $db->affected_rows();

        if($a>0){
            $data['status']='success';
            $data['message']='Customer berhasil ditambah.';
        } else {
            $data['status']='failed';
            $data['message']='Customer gagal ditambah.';
        }
        header('Content-Type: application/json');
        echo json_encode($data);
        break;

    case 'PUT':
        // Update an existing customer
        $_PUT = [];
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['ktp'])){
            $ktp = $_GET['ktp'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $customer->ktp = $_PUT['ktp'];
        $customer->nama = $_PUT['nama'];
        $customer->jk = $_PUT['jk'];
        $customer->kota = $_PUT['kota'];
        if($id>0){    
            $customer->update($id);
        }elseif($ktp>0){
            $customer->update_by_ktp($ktp);
        } else {
            
        } 
        
        $a = $db->affected_rows();

        if($a>0){
            $data['status']='success';
            $data['message']='Customer berhasil diperbarui.';
        } else {
            $data['status']='failed';
            $data['message']='Customer gagal diperbarui.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;

    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['ktp'])){
            $ktp = $_GET['ktp'];
        }
        if($id>0){    
            $customer->delete($id);
        }elseif($ktp>0){
            $customer->delete_by_ktp($ktp);
        } else {
            
        } 
        
        $a = $db->affected_rows();

        if($a>0){
            $data['status']='success';
            $data['message']='Customer berhasil dihapus.';
        } else {
            $data['status']='failed';
            $data['message']='Customer gagal dihapus.';
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
