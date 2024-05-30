# Examples  
![ex1](Examples/1.jpg)  
![ex2](Examples/2.jpg)  
![ex3](Examples/3.jpg)  
# Libraris  
To install all libraries:
<pre><code>pip install -r requirements.txt</code></pre>  
# Git commands  
Для клонирования репозитория:  
<pre><code>git clone ссылка на репозиторий</code></pre>  
Для создания репозитория (Если склонирован то не надо создавать репозиторий):
<pre><code>git init</code></pre>  
Для просмотра всех веток в репозитории:  
<pre><code>git branch</code></pre>  
Для создания новой ветки:  
<pre><code>git branch имя ветки</code></pre>  
Для переключения между ветками:  
<pre><code>git checkout имя ветки</code></pre>  
Для просмотра состояния всех файлов (Если все изменения сохранены - файлы не подсвечиваются):  
<pre><code>git status</code></pre>
Для сохранения изменений в ветке необходимо сделать commit:
<pre><code>git add .
git commit -m "Имя коммита"</code></pre>  
Для соединения локального и удалённого репозитория:
<pre><code>git remote add origin ссылка на репозиторий</code></pre>  
Для отправки всех коммитов в ветке на удалённый репозиторий:  
<pre><code>git push origin имя ветки</code></pre>  
Для получения изменений с удалённого репозитория (Находится в той же ветке, которая будет скачана):
<pre><code>git pull origin имя ветки</code></pre>