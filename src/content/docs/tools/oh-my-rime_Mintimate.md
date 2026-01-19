
---
title: oh-my-rime
---

### [Mintimate oh-my-rime](https://github.com/Mintimate/oh-my-rime)  ![GitHub Repo stars](https://img.shields.io/github/stars/Mintimate/oh-my-rime?style=social)

**项目核心内容总结：**  
oh-my-rime（薄荷输入法）是一个基于 Rime 输入法的模板方案，提供多种中文输入方案（如拼音、五笔）及自定义配置支持。  

**主要功能与特性：**  
1. **多输入方案支持**：包含薄荷拼音（全拼/双拼）、小鹤双拼、地球拼音、98/86五笔等，适配不同用户需求。  
2. **词库更新与定制**：采用万象词库（2025.07 更新），支持自定义词库扩展，通过 GitHub Action 自动同步雾凇、白霜等词库。  
3. **皮肤与配置自定义**：支持 Mac（鼠须管）和 Windows（小狼毫）的界面皮肤设置，提供 `custom.*.yaml` 文件实现个性化配置。  
4. **兼容性与优化**：支持九宫格输入（通过 `vv` 激活颜文字），优化 emoji 和纠错功能；Windows 7/XP 需使用特定版本 Weasel。  

**使用方法：**  
- 下载项目后，将配置文件复制到 Rime 的 `schema` 目录，覆盖原有文件（除 `custom_simple.dict.yaml`）。  
- 重新部署 Rime 输入法，通过快捷键（如 `Ctrl+Space`）切换输入方案。  
- 破坏性变更需注意：2025.07 后词库迁移至万象，需手动更新用户词典。  

**适用场景**：需要多语言输入、高度自定义输入法配置的用户，或希望优化中文输入体验的开发者。