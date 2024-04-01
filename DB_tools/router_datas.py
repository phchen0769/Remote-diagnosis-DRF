#!/usr/bin/env python
# encoding: utf-8

router_datas = [
    {
        "router_id": 1000,
        "sub_router": None,
        "path": "/profile",
        "component": "layout",
        "redirect": None,
        "name": "system",
        "title": "system",
        "icon": "user",
    },
    {
        "router_id": 2000,
        "sub_router": None,
        "path": "/user",
        "component": "layout",
        "redirect": "/user/manage",
        "name": "userManage",
        "title": "user",
        "icon": "personnel",
    },
    {
        "router_id": 2001,
        "sub_router": 2000,
        "path": "/user/manage",
        "component": "user-manage",
        "redirect": None,
        "name": None,
        "title": "userManage",
        "icon": "personnel-manage",
    },
    {
        "router_id": 2002,
        "sub_router": 2000,
        "path": "/user/info/:id",
        "component": "user-info",
        "hidden": True,
        "redirect": None,
        "name": None,
        "title": "userInfo",
        "icon": None,
    },
    {
        "router_id": 2003,
        "sub_router": 2000,
        "path": "/user/import",
        "component": "import",
        "hidden": True,
        "redirect": None,
        "name": "import",
        "title": "excelImport",
        "icon": None,
    },
    {
        "router_id": 2004,
        "sub_router": 2000,
        "path": "/user/role",
        "component": "role-list",
        "redirect": None,
        "name": None,
        "title": "roleList",
        "icon": "role",
    },
    {
        "router_id": 2005,
        "sub_router": 2000,
        "path": "/user/permission",
        "component": "permission-list",
        "redirect": None,
        "name": None,
        "title": "permissionList",
        "icon": "permission",
    },
    # 业务
    {
        "router_id": 3000,
        "sub_router": None,
        "path": "/article",
        "component": "layout",
        "redirect": "/article/ranking",
        "name": "articleRanking",
        "title": "article",
        "icon": "article",
    },
    {
        "router_id": 3001,
        "sub_router": 3000,
        "path": "/article/:id",
        "component": "article-detail",
        "hidden": True,
        "redirect": None,
        "name": None,
        "title": "articleDetail",
        "icon": None,
    },
    {
        "router_id": 3002,
        "sub_router": 3000,
        "path": "/article/create",
        "component": "article-create",
        "redirect": None,
        "name": None,
        "title": "articleCreate",
        "icon": "article-create",
    },
    {
        "router_id": 3003,
        "sub_router": 3000,
        "path": "/article/ranking",
        "component": "article-ranking",
        "redirect": "/article/ranking",
        "name": "articleRanking",
        "title": "articleRanking",
        "icon": "article-ranking",
    },
]
