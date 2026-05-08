#!/usr/bin/env python3
"""
GradHub Git提交和推送脚本
"""
import subprocess
from pathlib import Path

def run_command(cmd, cwd=None):
    """执行命令"""
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            capture_output=True,
            text=True,
            shell=True
        )
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return -1, "", str(e)

def main():
    repo_path = r"c:\Users\X1882\Desktop\github\final-year-project"

    print("=" * 60)
    print("🚀 GradHub Git 提交和推送")
    print("=" * 60)

    # 1. 检查状态
    print("\n[1] 📊 检查Git状态...")
    code, stdout, stderr = run_command("git status --short", cwd=repo_path)
    if code == 0:
        print(stdout if stdout else "✅ 工作目录干净")
    else:
        print(f"❌ 错误: {stderr}")

    # 2. 添加所有文件
    print("\n[2] 📦 添加所有文件到暂存区...")
    code, stdout, stderr = run_command("git add -A", cwd=repo_path)
    if code == 0:
        print("✅ 添加成功")
    else:
        print(f"❌ 添加失败: {stderr}")
        return

    # 3. 检查暂存文件
    print("\n[3] 📋 检查暂存的文件...")
    code, stdout, stderr = run_command("git status --short", cwd=repo_path)
    if code == 0:
        if stdout:
            print("暂存的文件:")
            print(stdout)
        else:
            print("没有文件需要提交")
            return
    else:
        print(f"❌ 错误: {stderr}")
        return

    # 4. 提交
    print("\n[4] 💾 提交更改...")
    commit_message = """🎓 GradHub v1.0 - 毕业项目导航站

✨ 主要更新:
- 完全重构为毕业项目导航站
- 唯美亮色调UI设计
- 多级导航系统(专业分类/技术栈/项目类型)
- 响应式移动端适配
- 流畅的动画效果

📦 新增文件:
- gradhub/ (完整网站)
- README.md (完整项目文档)
- LICENSE (MIT许可证)
- CONTRIBUTING.md (贡献指南)
- .gitignore (Git配置)
- .github/workflows/deploy.yml (自动部署)

🔧 技术栈:
- HTML5 + CSS3 + JavaScript
- CSS Variables + Flexbox + Grid
- 响应式设计
- GitHub Pages 自动部署
"""
    code, stdout, stderr = run_command(f'git commit -m "{commit_message}"', cwd=repo_path)
    if code == 0:
        print("✅ 提交成功")
        print(stdout)
    else:
        print(f"❌ 提交失败: {stderr}")
        return

    # 5. 查看提交历史
    print("\n[5] 📜 提交历史...")
    code, stdout, stderr = run_command("git log --oneline -3", cwd=repo_path)
    if code == 0:
        print(stdout)
    else:
        print(f"❌ 错误: {stderr}")

    # 6. 推送到GitHub
    print("\n[6] 🚀 推送到GitHub...")
    print("推送中...")
    code, stdout, stderr = run_command("git push -u origin main --force", cwd=repo_path)
    if code == 0:
        print("✅ 推送成功!")
        print(stdout)
    else:
        print(f"❌ 推送失败: {stderr}")
        print("\n提示: 如果推送被拒绝,可能是因为远程有新的提交。")
        print("可以使用 'git pull' 合并后再次推送。")

    print("\n" + "=" * 60)
    print("🎉 操作完成!")
    print("=" * 60)
    print("\n🌐 查看网站:")
    print("   https://badhope.github.io/final-year-project/")
    print("=" * 60)

if __name__ == "__main__":
    main()
