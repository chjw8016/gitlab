#!/usr/bin/env python
# coding=utf-8
import pymysql.cursors
import time

connection = pymysql.connect(host='dev.gammainfo.com',
                             port=3306,
                             user='root',
                             password='Gamma0903',
                             db='gitlab',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()


def addUser(id, name, user_name, email, state, is_admin, create_at):
    sql = "SELECT * FROM `users` WHERE `user_id`=%d" % (id)
    cursor.execute(sql)
    result = cursor.fetchone()
    time_at = int(time.time())
    if (result == None):
        sql = "INSERT INTO users (user_id, `name`,user_name,email,state,is_admin,created_at,create_time,update_time) VALUES ('%s', '%s', '%s', '%s', '%s', %d, %d, %d, %d)" % (
            id, name, user_name, email, state, is_admin, create_at, time_at, time_at)
        cursor.execute(sql)
        connection.commit()


def getProjects():
    sql = "SELECT * FROM `projects` "
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def getUsers():
    sql = "SELECT * FROM `users` "
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def addProjectMembers(project_id, user_id, user_name, name, state, access_level):
    sql = "SELECT * FROM `projects_members` WHERE `project_id`=%d and user_id=%d" % (project_id, user_id)
    cursor.execute(sql)
    result = cursor.fetchone()
    if (result == None):
        sql = "INSERT INTO projects_members (project_id,user_id,username, `name`, state, access_level) VALUES (%d, %d,'%s','%s','%s',%d)" % (
            project_id, user_id, user_name, name, state, access_level)
        cursor.execute(sql)
        connection.commit()


def addProject(id, name, description, default_branch, public, archived, visibility_level, ssh_url_to_repo,
               http_url_to_repo, web_url, name_with_namespace, path, path_with_namespace, issues_enabled,
               merge_requests_enabled, wiki_enabled, snippets_enabled, created_at, last_activity_at):
    sql = "SELECT * FROM `projects` WHERE `project_id`=%d" % (id)
    cursor.execute(sql)
    result = cursor.fetchone()
    time_at = int(time.time())
    if (result == None):
        sql = "INSERT INTO projects (project_id, `name`, description, default_branch, `public`, archived, visibility_level, ssh_url_to_repo,http_url_to_repo, web_url, name_with_namespace, path, path_with_namespace, issues_enabled,merge_requests_enabled, wiki_enabled, snippets_enabled, created_at, last_activity_at,update_time) VALUES (%d, '%s', '%s', '%s', '%s', '%s', %d, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', %d, %d, %d)" % (
            id, name, description, default_branch, public, archived, visibility_level, ssh_url_to_repo,
            http_url_to_repo,
            web_url, name_with_namespace, path, path_with_namespace, issues_enabled, merge_requests_enabled,
            wiki_enabled, snippets_enabled, created_at, last_activity_at, time_at)
        cursor.execute(sql)
        connection.commit()


def addCommit(project_id, id, short_id, title, author_name, author_email, created_at):
    sql = "select * from `commits` where commit_id='%s'" % (id)
    cursor.execute(sql)
    result = cursor.fetchone()
    if (result == None):
        sql = "insert into commits (project_id,commit_id, short_id, title, author_name, author_email, created_at) values (%s,'%s','%s','%s','%s','%s',%s)" % (
            project_id, id, short_id, title, author_name, author_email, created_at)
        cursor.execute(sql)
        connection.commit()


def addBranche(project_id, commit_id, commit_tree, name, message, author_name, author_email, commit_name, commit_email,
               authored_date,
               commited_date):
    sql = "select * from `projects_branches` where project_id=%d and `commit_id` = '%s' and commit_tree='%s'" % (
        project_id, commit_id, commit_tree)
    cursor.execute(sql)
    result = cursor.fetchone()
    if (result == None):
        sql = "insert into projects_branches (project_id,commit_id,commit_tree,`name`, message, author_name, author_email, commit_name, commit_email,authored_date,commited_date) values (%d,'%s','%s','%s','%s','%s','%s','%s','%s',%d,%d)" % (
            project_id, commit_id, commit_tree, name, message, author_name, author_email, commit_name, commit_email,
            authored_date,
            commited_date)
        cursor.execute(sql)
        connection.commit()


def addMergeRequest(project_id, mr_id, mr_iid, title, description, state, target_branch, source_branch,
                    source_project_id, target_project_id, author_id, assignee_id, author_name, assignee_name,
                    created_at, updated_at):
    sql = "select * from `projects_merge_requests` where project_id=%d and `mr_id` = %d and mr_iid=%d" % (
        project_id, mr_id, mr_iid)
    cursor.execute(sql)
    result = cursor.fetchone()
    if (result == None):
        sql = "insert into projects_merge_requests (project_id,mr_id,mr_iid,`title`, description, state, target_branch, source_branch, source_project_id,target_project_id,author_id,assignee_id,author_name,assignee_name,created_at,updated_at) values (%d,%d,%d,'%s','%s','%s','%s','%s',%d,%d,%d,%d,'%s','%s',%d,%d)" % (
            project_id, mr_id, mr_iid, title, description, state, target_branch, source_branch, source_project_id,
            target_project_id,
            author_id, assignee_id, author_name, assignee_name, created_at, updated_at)
        cursor.execute(sql)
        connection.commit()
