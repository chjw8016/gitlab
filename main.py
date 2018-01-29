#!/usr/bin/env python
# coding=utf-8
import gitlab

# 获取用户
gitlab.get_users()
# 获取项目
gitlab.get_projects()
# 获取项目成员
gitlab.get_project_members()
# 获取项目分支
gitlab.get_project_branches()
# 获取项目合并
gitlab.get_project_merge_requests()
# 获取项目提交
gitlab.get_project_commits()
print("OK")
