
---
title: hrms
---

### [frappe hrms](https://github.com/frappe/hrms)  ![GitHub Repo stars](https://img.shields.io/github/stars/frappe/hrms?style=social)

**项目名称**：Frappe HR（人力资源管理系统）

**项目简介**：  
Frappe HR 是一个开源、现代且易于使用的 HR 和薪资管理软件，适用于企业的人力资源管理全流程。它从 ERPNext 中独立出来，作为 Frappe 框架下的一个完整 HRMS 解决方案。

---

**主要功能**：

- **员工生命周期管理**：包括入职、晋升、调动、离职访谈等。
- **考勤与请假管理**：配置请假政策、查看节假日、考勤打卡、请假余额追踪。
- **费用报销与预支管理**：支持员工预支、报销申请，与 ERPNext 财务系统集成。
- **绩效管理**：设定目标、对齐关键绩效指标（KRA）、自我评估、绩效周期管理。
- **薪资与税务管理**：设置薪资结构、配置税务阶梯、运行标准薪资、处理额外薪资。
- **移动端应用**：支持请假申请、打卡、查看员工信息等。

---

**技术架构**：

- 基于 **Frappe Framework**（Python + JavaScript 全栈框架）。
- 使用 **Frappe UI**（Vue.js 前端组件库）构建现代用户界面。

---

**使用方法**：

- **托管部署**：可通过 [Frappe Cloud](https://frappecloud.com) 快速部署，无需本地配置。
- **Docker 部署**：需安装 Docker 和 docker-compose，运行命令：
  ```
  git clone https://github.com/frappe/hrms
  cd hrms/docker
  docker-compose up
  ```
- **本地部署**：需先安装 Bench，然后执行命令安装 HRMS 应用。

---

**学习与社区**：

- [Frappe School](https://frappe.school)：学习 Frappe 和 ERPNext 的课程。
- [文档](https://docs.frappe.io/hr)：详细的 HRMS 使用文档。
- [论坛](https://discuss.erpnext.com/)：社区交流与支持。
- [Telegram 群组](https://t.me/frappehr)：即时帮助与讨论。

---

**贡献指南**：

- 提交 issue 前请阅读 [Issue 指南](https://github.com/frappe/erpnext/wiki/Issue-Guidelines)。
- 安全漏洞报告请通过 [官网提交](https://erpnext.com/security)。
- Pull Request 需符合 [贡献指南](https://github.com/frappe/erpnext/wiki/Contribution-Guidelines)。