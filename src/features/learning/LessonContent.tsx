/** Rendu d'une leçon Markdown avec les blocs de provenance de la méthode (archives, complément, validé). */
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import remarkDirective from 'remark-directive';
import rehypeRaw from 'rehype-raw';
import { visit } from 'unist-util-visit';
import type { Root } from 'mdast';

const BLOCKS: Record<string, string> = {
  archives: '🟦 Archives UCL — ce que les examens interrogent (compilation d’étudiants)',
  complement: '🟨 Explication complémentaire — à valider',
  validated: '🟩 Explication complémentaire — validée',
};

function remarkProvenanceBlocks() {
  return (tree: Root) => {
    visit(tree, (node) => {
      if (node.type === 'containerDirective') {
        const name = (node as { name: string }).name;
        node.data = { hName: 'section', hProperties: { className: ['block', `block-${name}`], 'data-label': BLOCKS[name] ?? name } };
      }
    });
  };
}

export function LessonContent({ markdown }: { markdown: string }) {
  return (
    <div className="lesson">
      <ReactMarkdown
        remarkPlugins={[remarkGfm, remarkDirective, remarkProvenanceBlocks]}
        rehypePlugins={[rehypeRaw]}
        components={{
          section: ({ node: _n, ...props }) => {
            const label = (props as { 'data-label'?: string })['data-label'];
            return (
              <section {...props}>
                {label && <p className="block-label">{label}</p>}
                {props.children}
              </section>
            );
          },
          table: ({ node: _n, ...props }) => (
            <div className="table-wrap">
              <table {...props} />
            </div>
          ),
        }}
      >
        {markdown}
      </ReactMarkdown>
    </div>
  );
}
