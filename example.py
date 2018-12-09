import markdown_generator as mg

if __name__ == '__main__':
    with open('example.md', 'w') as f:
        writer = mg.Writer(f)
        writer.write('write()')
        writer.writeline()
        writer.writeline()
        writer.writeline('writeline()')
        writer.writelines([
            'writelines()1',
            'writelines()2'
        ])
        writer.write_hrule()

        writer.write_heading('heading1')
        for i in range(2, 7):
            writer.write_heading('heading{}'.format(i), i)

        writer.writeline(mg.emphasis('emphasis'))
        writer.writeline(mg.strong('strong'))
        writer.writeline(mg.strikethrough('strikethrough'))

        unordered = mg.List()
        unordered.append('unordered1')
        unordered.append(mg.emphasis('unordered2'))
        unordered.append('unordered3')
        writer.write(unordered)

        ordered = mg.List(ordered=True)
        unordered.append('ordered1')
        unordered.append(mg.emphasis('ordered2'))
        unordered.append('ordered3')
        writer.write(ordered)

        checklist = mg.CheckList()
        checklist.append('checklist1')
        checklist.append('checklist2', True)
        writer.write(checklist)

        link = mg.link('https://reddit.com', 'link text')
        writer.writeline(link)

        image = mg.Image(('https://github.com/adam-p/markdown-here/'
                          'raw/master/src/common/images/icon48.png'),
                         'my alt text')
        writer.writeline(image)

        code = mg.Code('Python')
        code.append("s = 'Python syntax highlighting'")
        code.append("print(s)")
        writer.write(code)
        writer.writeline()
        table = mg.Table()
        table.add_column('col1')
        table.add_column('col2', mg.Alignment.CENTER)
        table.add_column('col3', 2)
        for i in range(3):
            table.append(*['e{}f{}'.format(i, j) for j in range(3)])
        table.append()
        table.append(mg.strong('e5f1'), image)
        writer.write(table)

        blockquote = mg.BlockQuote()
        blockquote.append('A great man once said...')
        blockquote.append('- Wayne Gretzky')
        writer.write(blockquote)

        blockquote2 = mg.BlockQuote(level=2)
        blockquote2.append('- Michael Scott')
        writer.write(blockquote2)
