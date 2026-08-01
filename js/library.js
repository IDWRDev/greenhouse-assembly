(() => {
  const form = document.querySelector('[data-library-form]');
  const items = [...document.querySelectorAll('[data-library-item]')];
  if (!form || !items.length) return;

  const search = form.querySelector('[data-library-search]');
  const filter = form.querySelector('[data-library-filter]');
  const status = document.querySelector('[data-library-status]');
  const empty = document.querySelector('[data-library-empty]');
  const libraryName = form.dataset.library === 'resources' ? 'resources' : 'teaching pathways';

  const update = () => {
    const query = search.value.trim().toLocaleLowerCase();
    const topic = filter.value;
    let visible = 0;

    items.forEach((item) => {
      const matchesQuery = !query || `${item.dataset.search} ${item.textContent}`.toLocaleLowerCase().includes(query);
      const matchesTopic = topic === 'all' || item.dataset.topic === topic;
      const show = matchesQuery && matchesTopic;
      item.hidden = !show;
      if (show) visible += 1;
    });

    empty.hidden = visible !== 0;
    status.textContent = visible === items.length
      ? `Showing all ${items.length} ${libraryName}.`
      : `Showing ${visible} of ${items.length} ${libraryName}.`;
  };

  form.addEventListener('input', update);
  form.addEventListener('change', update);
  form.addEventListener('reset', () => window.requestAnimationFrame(update));
  update();
})();
