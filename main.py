from renamer import rename_files

folder = input("Enter folder path: ").strip()
prefix = input("Enter new filename prefix: ").strip()

result = rename_files(folder, prefix)

if result is None:
    print("❌ Folder not found.")
else:
    print(f"\n✅ Renamed {result} files successfully.")
