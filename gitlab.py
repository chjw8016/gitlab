#!/usr/bin/env python
# coding=utf-8
import requests
import model
import lib

base_url = 'https://code.gammainfo.com/api/v3'
headers = {'PRIVATE-TOKEN': 'r48K5-AxHFWTfVkKogNX'}


def get_users():
    page = 1
    while (page):
        url = base_url + "/users?per_page=100&page=" + str(page)
        request = requests.get(url, headers=headers, verify=False)
        if (request.status_code == 200):
            users = request.json()
            if (len(users) > 0):
                page = page + 1
                for user in users:
                    print(user)
                    model.addUser(user["id"], user["name"], user["username"], user["email"], user["state"],
                                  user["is_admin"],
                                  lib.utc_to_local(user["created_at"]))
            else:
                page = 0;
        else:
            page = 0;


def get_projects():
    page = 1
    while (page):
        url = base_url + "/projects?per_page=100&page=" + str(page)
        request = requests.get(url, headers=headers, verify=False)
        if (request.status_code == 200):
            projects = request.json()
            if (len(projects) > 0):
                page = page + 1
                for project in projects:
                    print(project)
                    model.addProject(project["id"], project["name"], project["description"], project["default_branch"],
                                     project["public"], project["archived"], project["visibility_level"],
                                     project["ssh_url_to_repo"], project["http_url_to_repo"], project["web_url"],
                                     project["name_with_namespace"], project["path"], project["path_with_namespace"],
                                     project["issues_enabled"], project["merge_requests_enabled"],
                                     project["wiki_enabled"], project["snippets_enabled"],
                                     lib.utc_to_local(project["created_at"]),
                                     lib.utc_to_local(project["last_activity_at"]))
            else:
                page = 0;
        else:
            page = 0;


def get_project_commits():
    projects = model.getProjects()
    for project in projects:
        page = 1
        id = project["project_id"]
        while (page):
            url = base_url + "/projects/" + str(id) + "/repository/commits?per_page=100&page=" + str(page)
            request = requests.get(url, headers=headers, verify=False)
            # print(request.status_code)
            if (request.status_code == 200):
                commits = request.json()
                # with open("log.txt", "a") as f:
                #    f.write(str(id) + "-" + str(len(commits)))
                if (len(commits) > 0):
                    page = page + 1
                    for commit in commits:
                        if (type(commit) is dict):
                            title = commit["title"].replace("'", "").replace("\\", "")
                            print(commit)
                            model.addCommit(id, commit["id"], commit["short_id"], title,
                                            commit["author_name"], commit["author_email"],
                                            lib.utc_to_local(commit["created_at"]))
                else:
                    page = 0
            else:
                # print(request.status_code)
                # with open("log.txt", "a") as f:
                #    f.write(str(id) + ":" + str(request.status_code))
                page = 0


def get_project_members():
    projects = model.getProjects()
    for project in projects:
        page = 1
        project_id = project["project_id"]
        while (page):
            url = base_url + "/projects/" + str(project_id) + "/members?per_page=100&page=" + str(page)
            request = requests.get(url, headers=headers, verify=False)
            if (request.status_code == 200):
                members = request.json()
                if (len(members) > 0):
                    page = page + 1
                    for member in members:
                        if (type(member) is dict):
                            print(member)
                            model.addProjectMembers(project_id, member["id"], member["username"], member["name"],
                                                    member["state"], member["access_level"])
                else:
                    page = 0
            else:
                # print(request.status_code)
                # with open("log.txt", "a") as f:
                #    f.write(str(id) + ":" + str(request.status_code))
                page = 0


def get_project_branches():
    projects = model.getProjects()
    for project in projects:
        project_id = project["project_id"]
        url = base_url + "/projects/" + str(project_id) + "/repository/branches"
        request = requests.get(url, headers=headers, verify=False)
        if (request.status_code == 200):
            branches = request.json()
            if (len(branches) > 0):
                for branche in branches:
                    if (type(branche) is dict):
                        print(branche)
                        model.addBranche(project_id, branche["commit"]["id"], branche["commit"]["tree"],
                                         branche["name"],
                                         branche["commit"]["message"].replace("'", ""),
                                         branche["commit"]["author"]["name"], branche["commit"]["author"]["email"],
                                         branche["commit"]["committer"]["name"],
                                         branche["commit"]["committer"]["email"],
                                         lib.utc_to_local(branche["commit"]["authored_date"],
                                                          "%Y-%m-%dT%H:%M:%S+08:00"),
                                         lib.utc_to_local(branche["commit"]["committed_date"],
                                                          "%Y-%m-%dT%H:%M:%S+08:00"))


def get_project_merge_requests():
    projects = model.getProjects()
    for project in projects:
        project_id = project["project_id"]
        url = base_url + "/projects/" + str(project_id) + "/merge_requests"
        request = requests.get(url, headers=headers, verify=False)
        if (request.status_code == 200):
            mrs = request.json()
            if (len(mrs) > 0):
                for mr in mrs:
                    if (type(mr) is dict):
                        print(mr)
                        if (mr["author"] == None):
                            assignee_id = 0
                            assignee_name = ""
                        else:
                            assignee_id = mr["author"]["id"]
                            assignee_name = mr["author"]["name"]
                        model.addMergeRequest(project_id, mr["id"], mr["iid"],
                                              mr["title"].replace("'", ""),
                                              mr["description"].replace("'", ""),
                                              mr["state"],
                                              mr["target_branch"],
                                              mr["source_branch"],
                                              mr["source_project_id"],
                                              mr["target_project_id"],
                                              mr["author"]["id"],
                                              assignee_id,
                                              mr["author"]["name"],
                                              assignee_name,
                                              lib.utc_to_local(mr["created_at"]),
                                              lib.utc_to_local(mr["updated_at"]))
