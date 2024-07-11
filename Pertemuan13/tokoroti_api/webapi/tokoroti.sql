-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 26, 2024 at 03:47 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `webapi`
--

-- --------------------------------------------------------

--
-- Table structure for table `tokoroti`
--

CREATE TABLE `tokoroti` (
  `id` int(11) NOT NULL,
  `kd_produk` char(6) DEFAULT NULL,
  `nama` char(20) DEFAULT NULL,
  `stok` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tokoroti`
--

INSERT INTO `tokoroti` (`id`, `kd_produk`, `nama`, `stok`) VALUES
(1, '895', 'Roti Tawar', 6),
(2, '712', 'Donat COklat', 4),
(3, '296', 'Brownis Kukus', 3);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tokoroti`
--
ALTER TABLE `tokoroti`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `kd_produk` (`kd_produk`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tokoroti`
--
ALTER TABLE `tokoroti`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
