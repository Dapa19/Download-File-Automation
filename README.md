<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Download File Management</title>
</head>
<body>

<h1>Download File Management</h1>

<p>This Python script automatically moves downloaded files to specific folders based on their file types. It is designed to help you organize your downloaded files by moving images, videos, and music files into designated directories.</p>

<h2>Features</h2>
<ul>
    <li><strong>Move Images:</strong> Automatically move image files (e.g., <code>.jpg</code>, <code>.jpeg</code>, <code>.png</code>, etc.) from the download folder to <code>D:/Saved Image</code>.</li>
    <li><strong>Move Videos:</strong> Automatically move video files (e.g., <code>.mp4</code>, <code>.avi</code>, <code>.mkv</code>, etc.) from the download folder to <code>D:/Saved Video</code>.</li>
    <li><strong>Move Music:</strong> Automatically move music files (e.g., <code>.mp3</code>, <code>.wav</code>, <code>.flac</code>, etc.) from the download folder to <code>D:/Saved Music</code>.</li>
    <li><strong>Move All:</strong> Option to move all images, videos, and music files at once.</li>
    <li><strong>User Interaction:</strong> Menu-driven interface allowing users to select the action they want to perform.</li>
</ul>

<h2>Requirements</h2>
<ul>
    <li>Python 3.x</li>
</ul>

<h2>Installation</h2>
<ol>
    <li>Clone the repository:
        <pre><code>git clone https://github.com/yourusername/download-file-management.git</code></pre>
    </li>
    <li>Navigate to the project directory:
        <pre><code>cd download-file-management</code></pre>
    </li>
    <li>Ensure you have Python 3 installed on your system. If not, download and install it from <a href="https://www.python.org/" target="_blank">Python's official website</a>.</li>
</ol>

<h2>Usage</h2>
<ol>
    <li>Open the script in your preferred Python environment or run it directly from the command line:
        <pre><code>python main.py</code></pre>
    </li>
    <li>Follow the on-screen instructions to choose the action you want to perform.
        <ul>
            <li><strong>1</strong>: Move Images</li>
            <li><strong>2</strong>: Move Videos</li>
            <li><strong>3</strong>: Move Music</li>
            <li><strong>4</strong>: Move All</li>
            <li><strong>0</strong>: Exit</li>
        </ul>
    </li>
</ol>

<h2>Customization</h2>
<ul>
    <li><strong>Folder Paths:</strong> Update the paths in the script to match your specific directory structure.</li>
    <li><strong>File Extensions:</strong> Modify the list of file extensions in the script if you want to include or exclude specific file types.</li>
</ul>

<h2>Author</h2>
<p><a href="https://github.com/Dapa19" target="_blank">Dafa aulia</a></p>

</body>
</html>
