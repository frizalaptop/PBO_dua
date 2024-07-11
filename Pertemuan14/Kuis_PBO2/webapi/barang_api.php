<?php
require_once 'database.php';
require_once 'Barang.php';

$db = new MySQLDatabase();
$barang = new Barang($db);
$id=0;
$kode=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];

// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kode'])){
            $kode = $_GET['kode'];
        }
        
        if($id>0){    
            $result = $barang->get_by_id($id);
        }elseif($kode>0){
            $result = $barang->get_by_kode($kode);
        } else {
            $result = $barang->get_all();
        }        
       
        $barang = array();
        while ($row = $result->fetch_assoc()) {
            $barang[] = $row;
        }
        header('Content-Type: application/json');
        echo json_encode($barang);
        break;

    case 'POST':
        // Add a new barang
        $barang->kode = $_POST['kode'];
        $barang->nama_barang = $_POST['nama_barang'];
        $barang->harga = $_POST['harga'];
        $barang->insert();
        
        $a = $db->affected_rows();

        if($a>0){
            $data['status']='success';
            $data['message']='Barang berhasil ditambah.';
        } else {
            $data['status']='failed';
            $data['message']='Barang gagal ditambah.';
        }
        header('Content-Type: application/json');
        echo json_encode($data);
        break;

    case 'PUT':
        // Update an existing barang
        $_PUT = [];
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kode'])){
            $kode = $_GET['kode'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $barang->kode = $_PUT['kode'];
        $barang->nama_barang = $_PUT['nama_barang'];
        $barang->harga = $_PUT['harga'];
        if($id>0){    
            $barang->update($id);
        }elseif($kode>0){
            $barang->update_by_kode($kode);
        } else {
            
        } 
        
        $a = $db->affected_rows();

        if($a>0){
            $data['status']='success';
            $data['message']='Barang berhasil diperbrui.';
        } else {
            $data['status']='failed';
            $data['message']='Barang gagal diperbarui.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;

    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kode'])){
            $kode = $_GET['kode'];
        }
        if($id>0){    
            $barang->delete($id);
        }elseif($kode>0){
            $barang->delete_by_kode($kode);
        } else {
            
        } 
        
        $a = $db->affected_rows();

        if($a>0){
            $data['status']='success';
            $data['message']='Barang berhasil dihapus.';
        } else {
            $data['status']='failed';
            $data['message']='Barang gagal dihapus.';
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
