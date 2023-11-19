-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Nov 20, 2023 alle 00:16
-- Versione del server: 10.4.28-MariaDB
-- Versione PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `progetto_tepsit`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `dipendenti_federico_ferretti`
--

CREATE TABLE `dipendenti_federico_ferretti` (
  `id_di` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `indirizzo` varchar(1024) NOT NULL,
  `telefono` varchar(100) NOT NULL,
  `cognome` varchar(100) NOT NULL,
  `mail` varchar(100) NOT NULL,
  `data_nascita` date NOT NULL,
  `posizione_lavorativa` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dump dei dati per la tabella `dipendenti_federico_ferretti`
--

INSERT INTO `dipendenti_federico_ferretti` (`id_di`, `nome`, `indirizzo`, `telefono`, `cognome`, `mail`, `data_nascita`, `posizione_lavorativa`) VALUES
(8, 'federico', 'via maggi ', '123456789', 'ferretti', 'federicoferretti@gmail.com', '2005-12-12', 'dipendente'),
(9, 'marco', 'via aprile', '987654321', 'battini', 'marobattini@gmail.com', '2003-11-08', 'dipendente'),
(10, 'silvio', 'via may', '147258369', 'berlusconi', 'silvio.berlusconi@gmail.com', '1936-09-29', 'capo');

-- --------------------------------------------------------

--
-- Struttura della tabella `zone_di_lavoro_federico_ferretti`
--

CREATE TABLE `zone_di_lavoro_federico_ferretti` (
  `id_zo` int(11) NOT NULL,
  `nome_zona` varchar(100) NOT NULL,
  `numero_clienti` int(11) NOT NULL,
  `cod_di` int(11) DEFAULT NULL,
  `indirizzo` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `zone_di_lavoro_federico_ferretti`
--

INSERT INTO `zone_di_lavoro_federico_ferretti` (`id_zo`, `nome_zona`, `numero_clienti`, `cod_di`, `indirizzo`) VALUES
(8, 'mandriolo', 18, 8, 'via mandrio '),
(9, 'canolicchio', 5, 8, 'via maresciallo '),
(10, 'repposty', 89, 10, 'via anna frank');

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `dipendenti_federico_ferretti`
--
ALTER TABLE `dipendenti_federico_ferretti`
  ADD PRIMARY KEY (`id_di`);

--
-- Indici per le tabelle `zone_di_lavoro_federico_ferretti`
--
ALTER TABLE `zone_di_lavoro_federico_ferretti`
  ADD PRIMARY KEY (`id_zo`),
  ADD KEY `cod_di` (`cod_di`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `dipendenti_federico_ferretti`
--
ALTER TABLE `dipendenti_federico_ferretti`
  MODIFY `id_di` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT per la tabella `zone_di_lavoro_federico_ferretti`
--
ALTER TABLE `zone_di_lavoro_federico_ferretti`
  MODIFY `id_zo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Limiti per le tabelle scaricate
--

--
-- Limiti per la tabella `zone_di_lavoro_federico_ferretti`
--
ALTER TABLE `zone_di_lavoro_federico_ferretti`
  ADD CONSTRAINT `zone_di_lavoro_federico_ferretti_ibfk_1` FOREIGN KEY (`cod_di`) REFERENCES `dipendenti_federico_ferretti` (`id_di`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
