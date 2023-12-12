import os
import shutil
import json

class FileNode:
    def __init__(self, name, is_directory=False):
        """
        Initialize a FileNode object.

        Parameters:
            name (str): The name of the file or directory.
            is_directory (bool): Indicates whether the node represents a directory.

        Attributes:
            name (str): The name of the file or directory.
            is_directory (bool): Indicates whether the node represents a directory.
            children (list): List of child nodes for directories.
        """
        self.name = name
        self.is_directory = is_directory
        self.children = []
class InMemoryFileSystem:
    def __init__(self):
        """
        Initialize the in-memory file system.

        Attributes:
            root (FileNode): The root directory of the file system.
            current_directory (FileNode): The current working directory.
        """
        self.root = FileNode('/', is_directory=True)
        self.current_directory = self.root

    def mkdir(self, directory_name):
        """
        Create a new directory.

        Parameters:
            directory_name (str): The name of the new directory
        """
        new_directory = FileNode(directory_name, is_directory=True)
        self.current_directory.children.append(new_directory)

    def cd(self, path):
        """
        Change the current directory.

        Parameters:
            path (str): The path to navigate to.
        """
        if path == '/':
            self.current_directory = self.root
        elif path.startswith('/'):
            self.current_directory = self._get_node_by_path(self.root, path)
        else:
            self.current_directory = self._get_node_by_path(self.current_directory, path)

    def ls(self, path=None):
        """
        List the contents of the current or specified directory.

        Parameters:
            path (str): The path of the directory to list (optional).
        """
        target_directory = self._get_node_by_path(self.current_directory, path) if path else self.current_directory
        for child in target_directory.children:
            print(child.name)

    def grep(self, pattern, file_path):
        """
        Search for a specified pattern in a file.

        Parameters:
            pattern (str): The pattern to search for.
            file_path (str): The path to the file.
        """
        file_node = self._get_node_by_path(self.current_directory, file_path)
        if file_node and not file_node.is_directory:
            with open(file_path, 'r') as file:
                for line in file:
                    if pattern in line:
                        print(line)

    def cat(self, file_path):
        """
        Display the contents of a file.

        Parameters:
            file_path (str): The path to the file.
        """
        file_node = self._get_node_by_path(self.current_directory, file_path)
        if file_node and not file_node.is_directory:
            with open(file_path, 'r') as file:
                print(file.read())

    def touch(self, file_name):
        """
        Create a new empty file.

        Parameters:
            file_name (str): The name of the new file.
        """
        new_file = FileNode(file_name)
        self.current_directory.children.append(new_file)

    def echo(self, text, file_path):
        """
        Write text to a file.

        Parameters:
            text (str): The text to write to the file.
            file_path (str): The path to the file.
        """
        file_node = self._get_node_by_path(self.current_directory, file_path)
        if file_node and not file_node.is_directory:
            with open(file_path, 'w') as file:
                file.write(text)

    def mv(self, source, destination):
        """
        Move a file or directory to another location.

        Parameters:
            source (str): The source file or directory path.
            destination (str): The destination path.
        """
        source_node = self._get_node_by_path(self.current_directory, source)
        if source_node:
            destination_node = self._get_node_by_path(self.current_directory, destination)
            if destination_node and destination_node.is_directory:
                source_node_parent = self._get_parent_node(self.current_directory, source)
                source_node_parent.children.remove(source_node)
                destination_node.children.append(source_node)

    def cp(self, source, destination):
        """
        Copy a file or directory to another location.

        Parameters:
            source (str): The source file or directory path.
            destination (str): The destination path.
        """
        source_node = self._get_node_by_path(self.current_directory, source)
        if source_node:
            destination_node = self._get_node_by_path(self.current_directory, destination)
            if destination_node and destination_node.is_directory:
                new_node = self._copy_node(source_node)
                destination_node.children.append(new_node)

    def rm(self, path):
        """
        Remove a file or directory.

        Parameters:
            path (str): The path of the file or directory to remove.
        """
        node_to_remove = self._get_node_by_path(self.current_directory, path)
        if node_to_remove:
            parent_node = self._get_parent_node(self.current_directory, path)
            parent_node.children.remove(node_to_remove)

    def _get_node_by_path(self, current_node, path):
        """
        Get a node by its path.

        Parameters:
            current_node (FileNode): The current node to start the search from.
            path (str): The path to the node.

        Returns:
            FileNode: The node found by the path.
        """
        components = path.strip('/').split('/')
        for component in components:
            found = False
            for child in current_node.children:
                if child.name == component and child.is_directory:
                    current_node = child
                    found = True
                    break
            if not found:
                return None
        return current_node

    def _get_parent_node(self, current_node, path):
        """
        Get the parent node of a node specified by its path.

        Parameters:
            current_node (FileNode): The current node to start the search from.
            path (str): The path to the node.

        Returns:
            FileNode: The parent node of the node specified by the path.
        """
        components = path.strip('/').split('/')
        parent_components = components[:-1]
        parent_path = '/' + '/'.join(parent_components)
        return self._get_node_by_path(current_node, parent_path)

    def _copy_node(self, node):
        """
        Recursively copy a node and its children.

        Parameters:
            node (FileNode): The node to copy.

        Returns:
            FileNode: The copied node.
        """
        new_node = FileNode(node.name, is_directory=node.is_directory)
        for child in node.children:
            new_node.children.append(self._copy_node(child))
        return new_node

    def save_state(self, file_path):
        """
        Save the current file system state to a file.

        Parameters:
            file_path (str): The path to the file where the state will be saved.
        """
        state_data = {
            'root': self.root,
            'current_directory': self.current_directory
        }
        with open(file_path, 'w') as file:
            json.dump(state_data, file)

    def load_state(self, file_path):
        """
        Load the file system state from a file.

        Parameters:
            file_path (str): The path to the file from which the state will be loaded.
        """
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                state_data = json.load(file)
                self.root = state_data.get('root', FileNode('/', is_directory=True))
                self.current_directory = state_data.get('current_directory', self.root)

def main():
    file_system = InMemoryFileSystem()

    # Check if there are command-line arguments
    import sys
    if len(sys.argv) > 1:
        command_line_args = json.loads(sys.argv[1])
        if 'save_state' in command_line_args and command_line_args['save_state'] == 'true':
            file_system.save_state(command_line_args.get('path', 'file_system_state.json'))
        elif 'load_state' in command_line_args and command_line_args['load_state'] == 'true':
            file_system.load_state(command_line_args.get('path', 'file_system_state.json'))

    while True:
        command = input("Enter command: ").split()

        if command[0] == 'exit':
            break

        operation = command[0]
        args = command[1:]

        if hasattr(file_system, operation):
            getattr(file_system, operation)(*args)
        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    main()
