<?php
require_once 'database.php';

class Tokoroti
{
    private $db;
    private $table = 'tokoroti';
    public $kd_produk = "";
    public $nama = "";
    public $stok = "";

    public function __construct(MySQLDatabase $db)
    {
        $this->db = $db;
    }

    public function get_all() 
    {
        $query = "SELECT * FROM $this->table";
        $result_set = $this->db->query($query);
        return $result_set;
    }

    public function get_by_id(int $id)
    {
        $query = "SELECT * FROM $this->table WHERE id = $id";
        $result_set = $this->db->query($query);   
        return $result_set;
    }

    public function get_by_kd_produk(int $kd_produk)
    {
        $query = "SELECT * FROM $this->table WHERE kd_produk = $kd_produk";
        $result_set = $this->db->query($query);   
        return $result_set;
    }

    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`kd_produk`, `nama`, `stok`) VALUES ('$this->kd_produk', '$this->nama', '$this->stok')";
        $this->db->query($query);
        return $this->db->insert_id();
    }

    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET `kd_produk` = '$this->kd_produk', `nama` = '$this->nama', `stok` = '$this->stok' WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }

    public function update_by_kd_produk($kd_produk): int
    {
        $query = "UPDATE $this->table SET `nama` = '$this->nama', `stok` = '$this->stok' WHERE kd_produk = $kd_produk";
        $this->db->query($query);
        return $this->db->affected_rows();
    }

    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }

    public function delete_by_kd_produk($kd_produk): int
    {
        $query = "DELETE FROM $this->table WHERE kd_produk = $kd_produk";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>