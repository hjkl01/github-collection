
---
title: k8s-device-plugin
---

### [NVIDIA k8s-device-plugin](https://github.com/NVIDIA/k8s-device-plugin)

**项目核心内容总结：**  
该项目是NVIDIA为Kubernetes设计的GPU设备插件，用于管理和调度GPU资源。其核心功能包括：  
1. **GPU资源管理**：支持多种Kubernetes版本，提供GPU设备插件部署、MIG（多实例GPU）策略配置、GPU产品命名规则自定义等功能。  
2. **部署方式**：  
   - 通过Helm Chart安装，支持独立模式（仅部署GPU特征发现）或集成模式（与设备插件联合部署）。  
   - 支持Docker镜像构建与运行，或直接编译运行（无需Docker）。  
3. **特性**：  
   - 兼容Kubernetes的CPUManager静态策略，支持共享/非共享GPU资源区分。  
   - 集成GPU特征发现（GFD）组件，自动检测并标注GPU型号、MIG配置等信息。  
   - 支持多版本管理，遵循语义化版本（SEMVER）规则，确保与Kubernetes API的兼容性。  
4. **使用场景**：适用于需要动态分配GPU资源的AI训练、推理等高性能计算任务，支持混合部署（MIG与非MIG混合使用）。  

**主要使用方法**：  
- **Helm安装**：通过Helm Chart配置参数（如`devicePlugin.enabled`、`migStrategy`等）部署插件或独立GFD组件。  
- **本地运行**：使用Docker构建镜像并运行，或直接编译源码执行。  
- **配置管理**：通过`--pass-device-specs`参数启用CPUManager兼容模式，或通过`renameByDefault`控制GPU资源命名规则。