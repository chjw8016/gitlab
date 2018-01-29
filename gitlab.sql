SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for commits
-- ----------------------------
DROP TABLE IF EXISTS `commits`;
CREATE TABLE `commits` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) DEFAULT '0',
  `commit_id` varchar(255) DEFAULT '',
  `short_id` varchar(255) DEFAULT '',
  `title` varchar(255) DEFAULT '',
  `author_name` varchar(255) DEFAULT '',
  `author_email` varchar(255) DEFAULT '',
  `created_at` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for projects
-- ----------------------------
DROP TABLE IF EXISTS `projects`;
CREATE TABLE `projects` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) DEFAULT '0' COMMENT 'ID',
  `name` varchar(255) DEFAULT '' COMMENT '项目名称',
  `description` varchar(255) DEFAULT '' COMMENT '项目描述',
  `default_branch` varchar(255) DEFAULT '' COMMENT '主分支',
  `public` varchar(255) DEFAULT '',
  `archived` varchar(255) DEFAULT '',
  `visibility_level` int(11) DEFAULT '0',
  `ssh_url_to_repo` varchar(255) DEFAULT '',
  `http_url_to_repo` varchar(255) DEFAULT '',
  `web_url` varchar(255) DEFAULT '',
  `name_with_namespace` varchar(255) DEFAULT '',
  `path` varchar(255) DEFAULT '',
  `path_with_namespace` varchar(255) DEFAULT '',
  `issues_enabled` varchar(255) DEFAULT '',
  `merge_requests_enabled` varchar(255) DEFAULT '',
  `wiki_enabled` varchar(255) DEFAULT '',
  `snippets_enabled` varchar(255) DEFAULT '',
  `created_at` int(11) DEFAULT '0',
  `last_activity_at` int(11) DEFAULT '0',
  `update_time` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for projects_branches
-- ----------------------------
DROP TABLE IF EXISTS `projects_branches`;
CREATE TABLE `projects_branches` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT '',
  `message` varchar(255) DEFAULT '',
  `author_name` varchar(255) DEFAULT '',
  `author_email` varchar(255) DEFAULT '',
  `commit_name` varchar(255) DEFAULT '',
  `commit_email` varchar(255) DEFAULT '',
  `authored_date` int(11) DEFAULT '0',
  `commited_date` int(11) DEFAULT '0',
  `project_id` int(11) DEFAULT '0',
  `commit_id` varchar(255) DEFAULT '',
  `commit_tree` varchar(255) DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for projects_members
-- ----------------------------
DROP TABLE IF EXISTS `projects_members`;
CREATE TABLE `projects_members` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) DEFAULT '0',
  `user_id` int(11) DEFAULT '0',
  `username` varchar(255) DEFAULT '',
  `name` varchar(255) DEFAULT '',
  `state` varchar(255) DEFAULT '',
  `access_level` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for projects_merge_requests
-- ----------------------------
DROP TABLE IF EXISTS `projects_merge_requests`;
CREATE TABLE `projects_merge_requests` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mr_id` int(11) DEFAULT '0',
  `mr_iid` int(11) DEFAULT '0',
  `project_id` int(11) DEFAULT '0',
  `title` varchar(255) DEFAULT '',
  `description` varchar(255) DEFAULT '',
  `state` varchar(255) DEFAULT '',
  `target_branch` varchar(255) DEFAULT '',
  `source_branch` varchar(255) DEFAULT '',
  `source_project_id` int(11) DEFAULT '0',
  `target_project_id` int(11) DEFAULT '0',
  `author_id` int(11) DEFAULT '0',
  `assignee_id` int(11) DEFAULT '0',
  `created_at` int(11) DEFAULT '0',
  `updated_at` int(11) DEFAULT '0',
  `author_name` varchar(255) DEFAULT '',
  `assignee_name` varchar(255) DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT '' COMMENT '显示名称',
  `user_name` varchar(255) DEFAULT '' COMMENT '账户',
  `state` varchar(255) DEFAULT '' COMMENT '状态',
  `user_id` int(11) DEFAULT '0' COMMENT 'ID',
  `is_admin` tinyint(4) DEFAULT '0' COMMENT '是否管理员',
  `email` varchar(255) DEFAULT '' COMMENT '邮箱',
  `created_at` int(11) DEFAULT '0' COMMENT '加入时间',
  `create_time` int(11) DEFAULT '0',
  `update_time` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
