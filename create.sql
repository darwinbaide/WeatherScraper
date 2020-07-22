/* These are the create commands for the weather tables */

CREATE TABLE `forecast` (
  `num` int(11) NOT NULL,
  `oneDate` varchar(45) DEFAULT NULL,
  `oneTemp` varchar(45) DEFAULT NULL,
  `oneForecast` varchar(45) DEFAULT NULL,
  `oneChance` varchar(45) DEFAULT NULL,
  `twoDate` varchar(45) DEFAULT NULL,
  `twoTemp` varchar(45) DEFAULT NULL,
  `twoForecast` varchar(45) DEFAULT NULL,
  `twoChance` varchar(45) DEFAULT NULL,
  `threeDate` varchar(45) DEFAULT NULL,
  `threeTemp` varchar(45) DEFAULT NULL,
  `threeForecast` varchar(45) DEFAULT NULL,
  `threeChance` varchar(45) DEFAULT NULL,
  `fourDate` varchar(45) DEFAULT NULL,
  `fourTemp` varchar(45) DEFAULT NULL,
  `fourForecast` varchar(45) DEFAULT NULL,
  `fourChance` varchar(45) DEFAULT NULL,
  `fiveDate` varchar(45) DEFAULT NULL,
  `fiveTemp` varchar(45) DEFAULT NULL,
  `fiveForecast` varchar(45) DEFAULT NULL,
  `fiveChance` varchar(45) DEFAULT NULL,
  `sixDate` varchar(45) DEFAULT NULL,
  `sixTemp` varchar(45) DEFAULT NULL,
  `sixForecast` varchar(45) DEFAULT NULL,
  `sixChance` varchar(45) DEFAULT NULL,
  `timestamp` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;






CREATE TABLE `today` (
  `num` int(11) NOT NULL AUTO_INCREMENT,
  `forecast` varchar(45) DEFAULT NULL,
  `rainChance` varchar(45) DEFAULT NULL,
  `humidity` varchar(45) DEFAULT NULL,
  `sunrise` varchar(45) DEFAULT NULL,
  `sunset` varchar(45) DEFAULT NULL,
  `wind` varchar(45) DEFAULT NULL,
  `high` varchar(45) DEFAULT NULL,
  `low` varchar(45) DEFAULT NULL,
  `current` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`num`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;