-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Feb 05, 2019 at 07:05 AM
-- Server version: 5.5.8
-- PHP Version: 5.3.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `hallallotment`
--

-- --------------------------------------------------------

--
-- Table structure for table `adminlogin`
--

CREATE TABLE IF NOT EXISTS `adminlogin` (
  `uname` varchar(48) NOT NULL,
  `pwd` varchar(68) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `adminlogin`
--

INSERT INTO `adminlogin` (`uname`, `pwd`) VALUES
('admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `allotment`
--

CREATE TABLE IF NOT EXISTS `allotment` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `hallno` varchar(50) NOT NULL,
  `regno` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `subject` varchar(50) NOT NULL,
  `examdate` varchar(50) NOT NULL,
  `sess` varchar(50) NOT NULL,
  `others` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `allotment`
--

INSERT INTO `allotment` (`id`, `hallno`, `regno`, `name`, `subject`, `examdate`, `sess`, `others`) VALUES
(5, '101', '100BSC01', 'a', 'cs', '5/2/2019', 'FN', 'nil');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE IF NOT EXISTS `student` (
  `name` varchar(50) NOT NULL,
  `user` varchar(50) NOT NULL,
  `pwd` varchar(50) NOT NULL,
  `regno` varchar(50) NOT NULL,
  `dept` varchar(50) NOT NULL,
  `year` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`name`, `user`, `pwd`, `regno`, `dept`, `year`, `email`) VALUES
('kjgh', 'kjgh', 'kjhg', 'kjhg', 'kjgh', 'jhg', 'kjhg'),
('a', 'a', 'a', 'a', 'admin', 'a', 'a');
