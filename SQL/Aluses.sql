-- MySQL Script generated by MySQL Workbench
-- vie 14 sep 2018 10:07:28 -03
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema Aluses
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `Aluses` ;

-- -----------------------------------------------------
-- Schema Aluses
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Aluses` DEFAULT CHARACTER SET utf8 ;
USE `Aluses` ;

-- -----------------------------------------------------
-- Table `Aluses`.`PlaneModel`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Aluses`.`PlaneModel` ;

CREATE TABLE IF NOT EXISTS `Aluses`.`PlaneModel` (
  `code` INT(11) NOT NULL AUTO_INCREMENT,
  `seatQuantity` INT(11) NOT NULL,
  PRIMARY KEY (`code`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `Aluses`.`Plane`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Aluses`.`Plane` ;

CREATE TABLE IF NOT EXISTS `Aluses`.`Plane` (
  `idPlane` INT(11) NOT NULL AUTO_INCREMENT,
  `modelCode` INT(11) NOT NULL,
  `constructionDay` DATE NOT NULL,
  PRIMARY KEY (`idPlane`),
  CONSTRAINT `fk_Plane_PlaneModel1`
    FOREIGN KEY (`modelCode`)
    REFERENCES `Aluses`.`PlaneModel` (`code`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE INDEX `fk_Plane_PlaneModel1_idx` ON `Aluses`.`Plane` (`modelCode` ASC);


-- -----------------------------------------------------
-- Table `Aluses`.`Flight`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Aluses`.`Flight` ;

CREATE TABLE IF NOT EXISTS `Aluses`.`Flight` (
  `idFlight` INT(11) NOT NULL AUTO_INCREMENT,
  `departure` VARCHAR(45) NOT NULL,
  `arrival` VARCHAR(45) NOT NULL,
  `idPlane` INT(11) NOT NULL,
  `flightDepartureDatetime` DATETIME NOT NULL,
  `flightArrivalDatetime` DATETIME NOT NULL,
  PRIMARY KEY (`idFlight`),
  CONSTRAINT `fk_Flight_Plane1`
    FOREIGN KEY (`idPlane`)
    REFERENCES `Aluses`.`Plane` (`idPlane`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE INDEX `fk_Flight_Plane1_idx` ON `Aluses`.`Flight` (`idPlane` ASC);


-- -----------------------------------------------------
-- Table `Aluses`.`User`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Aluses`.`User` ;

CREATE TABLE IF NOT EXISTS `Aluses`.`User` (
  `idUser` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `lastname` VARCHAR(45) NOT NULL,
  `mail` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  `administrador` TINYINT(1) NULL DEFAULT NULL,
  PRIMARY KEY (`idUser`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `Aluses`.`Seats`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Aluses`.`Seats` ;

CREATE TABLE IF NOT EXISTS `Aluses`.`Seats` (
  `seatNumber` INT(11) NOT NULL AUTO_INCREMENT,
  `modelCode` INT(11) NOT NULL,
  `seatClass` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`seatNumber`),
  CONSTRAINT `fk_Seats_PlaneModel1`
    FOREIGN KEY (`modelCode`)
    REFERENCES `Aluses`.`PlaneModel` (`code`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE INDEX `fk_Seats_PlaneModel1_idx` ON `Aluses`.`Seats` (`modelCode` ASC);


-- -----------------------------------------------------
-- Table `Aluses`.`Flight_has_User`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Aluses`.`Flight_has_User` ;

CREATE TABLE IF NOT EXISTS `Aluses`.`Flight_has_User` (
  `idFlight` INT(11) NOT NULL,
  `idUser` INT(11) NOT NULL,
  `seatNumber` INT(11) NOT NULL,
  PRIMARY KEY (`idFlight`, `idUser`),
  CONSTRAINT `fk_Flight_has_Person_Flight1`
    FOREIGN KEY (`idFlight`)
    REFERENCES `Aluses`.`Flight` (`idFlight`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Flight_has_Person_Person1`
    FOREIGN KEY (`idUser`)
    REFERENCES `Aluses`.`User` (`idUser`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Flight_has_Person_Seats1`
    FOREIGN KEY (`seatNumber`)
    REFERENCES `Aluses`.`Seats` (`seatNumber`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE INDEX `fk_Flight_has_Person_Person1_idx` ON `Aluses`.`Flight_has_User` (`idUser` ASC);

CREATE INDEX `fk_Flight_has_Person_Flight1_idx` ON `Aluses`.`Flight_has_User` (`idFlight` ASC);

CREATE INDEX `fk_Flight_has_Person_Seats1_idx` ON `Aluses`.`Flight_has_User` (`seatNumber` ASC);


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
