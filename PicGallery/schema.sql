
-- CREATE DATABASE `picgallerytest` /*!40100 DEFAULT CHARACTER SET utf8 */;
drop table if exists images;
CREATE TABLE `images` (
  `id` integer primary key autoincrement,
  `name` text DEFAULT NULL,
  `extention` text DEFAULT NULL,
  `username` text DEFAULT NULL,
  `tag` text DEFAULT NULL,
  `dd` text DEFAULT NULL
);
drop table if exists comments;
CREATE TABLE `comments` (
  `id` integer NOT NULL,
  `idimage` integer NOT NULL,
  `comments` text DEFAULT NULL,
  `username` text DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `idimage` FOREIGN KEY (`idimage`) REFERENCES `images` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) ;


insert into images values(1,"DSC_0146.jpg","image/jpeg","Traveller","Grasslands","2016-09-29");
insert into images values(2,"DSC_0082.jpg","image/jpeg","Traveller","Sea","2016-09-29");
insert into images values(3,"DSC_0079.jpg","image/jpeg","Partner","Sea","2016-09-29");
insert into images values(4,"DSC_0004.jpg","image/jpeg","Traveller","Forest","2016-09-29");
insert into images values(5,"DSC_0001.jpg","image/jpeg","Partner","Forest","2016-09-29");

insert into comments values(1, 1, 'Good Work', "Visitor");
insert into comments values(2, 1, "Beatify hill","Partner");
