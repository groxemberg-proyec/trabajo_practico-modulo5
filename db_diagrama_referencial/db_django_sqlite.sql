-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema db_django_sqlite
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema db_django_sqlite
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `db_django_sqlite` DEFAULT CHARACTER SET utf8 ;
USE `db_django_sqlite` ;

-- -----------------------------------------------------
-- Table `db_django_sqlite`.`gestiones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_django_sqlite`.`gestiones` (
  `idGestion` INT NOT NULL AUTO_INCREMENT,
  `nombreGestion` VARCHAR(4) NOT NULL DEFAULT '2000',
  `estado` TINYINT UNSIGNED NOT NULL DEFAULT 1,
  `fechaRegistro` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fechaActualizacion` TIMESTAMP NULL,
  PRIMARY KEY (`idGestion`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_django_sqlite`.`periodos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_django_sqlite`.`periodos` (
  `idPeriodo` INT NOT NULL AUTO_INCREMENT,
  `idGestion` INT NOT NULL,
  `nombrePeriodo` VARCHAR(45) NOT NULL,
  `posicionOrdinal` TINYINT UNSIGNED NOT NULL DEFAULT 0,
  `estado` TINYINT UNSIGNED NOT NULL DEFAULT 1,
  `fechaRegistro` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fechaActualizacion` TIMESTAMP NULL,
  PRIMARY KEY (`idPeriodo`),
  INDEX `fk_periodos_gestiones1_idx` (`idGestion` ASC) VISIBLE,
  CONSTRAINT `fk_periodos_gestiones1`
    FOREIGN KEY (`idGestion`)
    REFERENCES `db_django_sqlite`.`gestiones` (`idGestion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_django_sqlite`.`colegios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_django_sqlite`.`colegios` (
  `idColegio` INT NOT NULL AUTO_INCREMENT,
  `nombreColegio` VARCHAR(45) NOT NULL,
  `direccion` VARCHAR(180) NOT NULL,
  `telefono` VARCHAR(15) NOT NULL,
  `sitioWeb` VARCHAR(45) NOT NULL,
  `estado` TINYINT UNSIGNED NOT NULL DEFAULT 1,
  `fechaRegistro` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fechaActualizacion` TIMESTAMP NULL,
  PRIMARY KEY (`idColegio`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_django_sqlite`.`personas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_django_sqlite`.`personas` (
  `idPersona` INT NOT NULL AUTO_INCREMENT,
  `idColegio` INT NOT NULL,
  `nombres` VARCHAR(80) NOT NULL,
  `apellidoPaterno` VARCHAR(45) NOT NULL,
  `apellidoMaterno` VARCHAR(45) NOT NULL,
  `cedulaIdentidadNumero` VARCHAR(9) NOT NULL,
  `cedulaIdentidadExpedido` VARCHAR(20) NOT NULL,
  `tipoPerfil` VARCHAR(45) NOT NULL DEFAULT 'SOCIO',
  `estado` TINYINT UNSIGNED NOT NULL DEFAULT 1,
  `fechaRegistro` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fechaActualizacion` TIMESTAMP NULL,
  PRIMARY KEY (`idPersona`),
  INDEX `fk_personas_colegios1_idx` (`idColegio` ASC) VISIBLE,
  CONSTRAINT `fk_personas_colegios1`
    FOREIGN KEY (`idColegio`)
    REFERENCES `db_django_sqlite`.`colegios` (`idColegio`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_django_sqlite`.`niveles`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_django_sqlite`.`niveles` (
  `idNivel` INT NOT NULL AUTO_INCREMENT,
  `nombreNivel` VARCHAR(20) NOT NULL,
  `posicionOrdinal` TINYINT UNSIGNED NOT NULL DEFAULT 0,
  `estado` TINYINT UNSIGNED NOT NULL DEFAULT 1,
  `fechaRegistro` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fechaActualizacion` TIMESTAMP NULL,
  PRIMARY KEY (`idNivel`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_django_sqlite`.`grados`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_django_sqlite`.`grados` (
  `idGrado` INT NOT NULL AUTO_INCREMENT,
  `idNivel` INT NOT NULL,
  `nombreGrado` VARCHAR(45) NOT NULL,
  `posicionOrdinal` TINYINT UNSIGNED NOT NULL DEFAULT 0,
  `estado` TINYINT UNSIGNED NOT NULL DEFAULT 1,
  `fechaRegistro` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fechaActualizacion` TIMESTAMP NULL,
  PRIMARY KEY (`idGrado`),
  INDEX `fk_grados_niveles1_idx` (`idNivel` ASC) VISIBLE,
  CONSTRAINT `fk_grados_niveles1`
    FOREIGN KEY (`idNivel`)
    REFERENCES `db_django_sqlite`.`niveles` (`idNivel`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_django_sqlite`.`paralelos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_django_sqlite`.`paralelos` (
  `idParalelo` INT NOT NULL AUTO_INCREMENT,
  `nombreParalelo` CHAR NOT NULL,
  PRIMARY KEY (`idParalelo`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_django_sqlite`.`cursos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_django_sqlite`.`cursos` (
  `idCurso` INT NOT NULL AUTO_INCREMENT,
  `idGrado` INT NOT NULL,
  `idParalelo` INT NOT NULL,
  `nombreCurso` VARCHAR(100) NOT NULL,
  `paralelo` CHAR NOT NULL DEFAULT 'A',
  `estado` TINYINT UNSIGNED NOT NULL DEFAULT 1,
  `fechaRegistro` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fechaActualizacion` TIMESTAMP NULL,
  PRIMARY KEY (`idCurso`),
  INDEX `fk_cursos_grados1_idx` (`idGrado` ASC) VISIBLE,
  INDEX `fk_cursos_paralelos1_idx` (`idParalelo` ASC) VISIBLE,
  CONSTRAINT `fk_cursos_grados1`
    FOREIGN KEY (`idGrado`)
    REFERENCES `db_django_sqlite`.`grados` (`idGrado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_cursos_paralelos1`
    FOREIGN KEY (`idParalelo`)
    REFERENCES `db_django_sqlite`.`paralelos` (`idParalelo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_django_sqlite`.`estudiantes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_django_sqlite`.`estudiantes` (
  `idEstudiante` INT NOT NULL AUTO_INCREMENT,
  `idPersona` INT NOT NULL,
  `idCurso` INT NOT NULL,
  `saludAlergias` VARCHAR(200) NOT NULL,
  `saludGrupoSanguineo` VARCHAR(3) NOT NULL,
  `saludDatosMedicosImportantes` VARCHAR(200) NOT NULL,
  `estado` TINYINT UNSIGNED NOT NULL DEFAULT 1,
  `fechaRegistro` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fechaActualizacion` TIMESTAMP NULL,
  PRIMARY KEY (`idEstudiante`),
  INDEX `fk_estudiantes_personas_idx` (`idPersona` ASC) VISIBLE,
  INDEX `fk_estudiantes_cursos1_idx` (`idCurso` ASC) VISIBLE,
  CONSTRAINT `fk_estudiantes_personas`
    FOREIGN KEY (`idPersona`)
    REFERENCES `db_django_sqlite`.`personas` (`idPersona`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_estudiantes_cursos1`
    FOREIGN KEY (`idCurso`)
    REFERENCES `db_django_sqlite`.`cursos` (`idCurso`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_django_sqlite`.`profesores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_django_sqlite`.`profesores` (
  `idProfesor` INT NOT NULL AUTO_INCREMENT,
  `idPersona` INT NOT NULL,
  `numeroCelular` VARCHAR(15) NOT NULL,
  `estado` TINYINT UNSIGNED NOT NULL DEFAULT 1,
  `fechaRegistro` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fechaActualizacion` TIMESTAMP NULL,
  PRIMARY KEY (`idProfesor`),
  INDEX `fk_profesores_personas1_idx` (`idPersona` ASC) VISIBLE,
  CONSTRAINT `fk_profesores_personas1`
    FOREIGN KEY (`idPersona`)
    REFERENCES `db_django_sqlite`.`personas` (`idPersona`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_django_sqlite`.`asignaturas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_django_sqlite`.`asignaturas` (
  `idAsignatura` INT NOT NULL AUTO_INCREMENT,
  `idProfesor` INT NOT NULL,
  `nombreAsignatura` VARCHAR(45) NOT NULL,
  `estado` TINYINT UNSIGNED NOT NULL DEFAULT 1,
  `fechaRegistro` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fechaActualizacion` TIMESTAMP NULL,
  PRIMARY KEY (`idAsignatura`),
  INDEX `fk_asignaturas_profesores1_idx` (`idProfesor` ASC) VISIBLE,
  CONSTRAINT `fk_asignaturas_profesores1`
    FOREIGN KEY (`idProfesor`)
    REFERENCES `db_django_sqlite`.`profesores` (`idProfesor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_django_sqlite`.`calificaciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_django_sqlite`.`calificaciones` (
  `idCalificacion` INT NOT NULL AUTO_INCREMENT,
  `idPeriodo` INT NOT NULL,
  `idAsignatura` INT NOT NULL,
  `idEstudiante` INT NOT NULL,
  `calificacionGeneral` TINYINT UNSIGNED NOT NULL DEFAULT 1,
  `calificacionSer` TINYINT UNSIGNED NOT NULL DEFAULT 1,
  `calificacionSaber` TINYINT UNSIGNED NOT NULL DEFAULT 1,
  `calificacionHacer` TINYINT UNSIGNED NOT NULL DEFAULT 1,
  `calificacionDecidir` TINYINT UNSIGNED NOT NULL DEFAULT 1,
  `calificacionAutoevaluacion` TINYINT UNSIGNED NOT NULL DEFAULT 1,
  `estado` TINYINT UNSIGNED NOT NULL DEFAULT 1,
  `fechaRegistro` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fechaActualizacion` TIMESTAMP NULL,
  PRIMARY KEY (`idCalificacion`),
  INDEX `fk_calificaciones_periodos1_idx` (`idPeriodo` ASC) VISIBLE,
  INDEX `fk_calificaciones_estudiantes1_idx` (`idEstudiante` ASC) VISIBLE,
  INDEX `fk_calificaciones_asignaturas1_idx` (`idAsignatura` ASC) VISIBLE,
  CONSTRAINT `fk_calificaciones_periodos1`
    FOREIGN KEY (`idPeriodo`)
    REFERENCES `db_django_sqlite`.`periodos` (`idPeriodo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_calificaciones_estudiantes1`
    FOREIGN KEY (`idEstudiante`)
    REFERENCES `db_django_sqlite`.`estudiantes` (`idEstudiante`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_calificaciones_asignaturas1`
    FOREIGN KEY (`idAsignatura`)
    REFERENCES `db_django_sqlite`.`asignaturas` (`idAsignatura`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
