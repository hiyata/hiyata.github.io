---
layout: default
title: Sequence-Based Virus Host Prediction — A Curated Dataset and Generalizable Framework
category: virology
excerpt: A 58,046-genome dataset and neural network framework that predicts whether a virus can infect humans directly from raw genome sequence, no alignment or annotation required. Published in Virus Evolution.
presented_at: Virus Evolution, 2026
permalink: /virus-host-classifier/
---

<article class="post-page">
  <div class="post-page-wrapper">
    <header class="post-page-header">
      <a class="post-page-back" href="{{ '/projects' | relative_url }}">&larr; Projects</a>
      <p class="post-page-kicker">Case Study &middot; Published Research</p>
      <h1 class="post-page-title">Sequence-Based Virus Host Prediction</h1>
      <p class="post-page-meta">
        Carbajo Jr AL, Vensko TA, Pellett PE &middot; <em>Virus Evolution</em>, 2026, 12(1), veag009
        <span class="post-page-meta-sep">&middot;</span> <a href="https://doi.org/10.1093/ve/veag009" target="_blank" rel="noopener">doi.org/10.1093/ve/veag009</a>
      </p>
    </header>

    <div class="post-page-content">

      <p>
        Can you tell whether a virus infects humans just by looking at its genome, no alignment,
        no annotation, no prior knowledge of what gene does what? That's the question behind
        this project: a curated dataset of 58,046 virus genomes and a neural network framework
        that reads raw nucleotide sequence and predicts human-host compatibility directly.
      </p>

      <div class="stat-strip">
        <div class="stat-strip-item">
          <span class="stat-strip-value">58,046</span>
          <span class="stat-strip-label">curated genomes across 15 virus families</span>
        </div>
        <div class="stat-strip-item">
          <span class="stat-strip-value">0.820</span>
          <span class="stat-strip-label">best MCC, neural net at k = 5</span>
        </div>
        <div class="stat-strip-item">
          <span class="stat-strip-value">97.2%</span>
          <span class="stat-strip-label">accuracy of AI-assisted host labeling</span>
        </div>
        <div class="stat-strip-item">
          <span class="stat-strip-value">2.61</span>
          <span class="stat-strip-label">Cohen's d separating human vs. animal coronaviruses</span>
        </div>
      </div>

      <h2>The problem: GenBank's metadata is a mess</h2>
      <p>
        Genomic signatures of host adaptation exist in virus sequences, but repositories like
        GenBank store the metadata needed to study them in wildly inconsistent formats. A host
        field might read <em>"Homo sapiens,"</em> or <em>"26-day-old piglet,"</em> or nothing at
        all, with the real information buried in an isolation-source note like
        <em>"asymptomatic carrier."</em> That inconsistency is exactly what has kept this kind of
        pan-virome analysis out of reach: you can't train a model on a label you can't trust.
      </p>

      <h2>Building a dataset worth training on</h2>
      <p>
        We started from 82,513 complete genomes across 15 virus families, chosen to span
        different genome architectures (dsDNA, ssRNA, dsRNA, reverse-transcribing) and a mix of
        strictly human, strictly non-human, and dual-host viruses. After filtering out partial,
        unverified, and non-standard sequences, we labeled every remaining genome for human-host
        compatibility using a three-tier system of increasing sophistication.
      </p>

      <div class="figure-row">
        <div class="stat-strip-item" style="border-radius: var(--radius-md); border: 1px solid var(--border);">
          <span class="stat-strip-label" style="text-transform: uppercase; font-family: var(--mono); letter-spacing: 0.05em; color: var(--accent);">Tier 1 &middot; String matching</span>
          <p style="margin: 0.6rem 0 0; color: var(--ink-soft); font-size: 0.95rem;">Direct matches to standard scientific nomenclature, e.g. an explicit <em>"Homo sapiens"</em> host field.</p>
        </div>
        <div class="stat-strip-item" style="border-radius: var(--radius-md); border: 1px solid var(--border);">
          <span class="stat-strip-label" style="text-transform: uppercase; font-family: var(--mono); letter-spacing: 0.05em; color: var(--accent);">Tier 2 &middot; Pattern lookup</span>
          <p style="margin: 0.6rem 0 0; color: var(--ink-soft); font-size: 0.95rem;">A curated regex dictionary normalizes informal terms, e.g. mapping <em>"26-day-old piglet"</em> to <em>Sus scrofa</em>.</p>
        </div>
        <div class="stat-strip-item" style="border-radius: var(--radius-md); border: 1px solid var(--border);">
          <span class="stat-strip-label" style="text-transform: uppercase; font-family: var(--mono); letter-spacing: 0.05em; color: var(--accent);">Tier 3 &middot; AI inference</span>
          <p style="margin: 0.6rem 0 0; color: var(--ink-soft); font-size: 0.95rem;">Gemini 1.5 Flash reads clinical context, e.g. inferring <em>Homo sapiens</em> from <em>"asymptomatic carrier"</em> in a Hepatitis B record.</p>
        </div>
      </div>

      <p>
        We manually checked 1,000 of Tier 3's AI-powered calls against GenBank records and the
        primary literature. It was right 97.2% of the time, and the misses clustered almost
        entirely around enteroviruses, where the host information genuinely isn't in the
        metadata, it's only findable by tracking down the associated paper.
      </p>

      <p>
        The final set: 58,046 genomes, split almost evenly between human-associated (52.0%) and
        non-human-associated (48.0%) sequences. To keep the model honest, we didn't split
        train/validation/test randomly, near-duplicate strains would leak across the boundary.
        Instead we clustered 6-mer profiles with UMAP and DBSCAN and kept every sequence in a
        cluster on the same side of the split.
      </p>

      <h2>Teaching a model to read raw sequence</h2>
      <p>
        The input feature is deliberately simple: k-mer frequency, the normalized count of every
        possible substring of length <em>k</em> in a genome, for k = 3 through 8. No alignment,
        no gene annotation, no reference genome required, just how often each short nucleotide
        pattern shows up. We benchmarked this feature against three model families: logistic
        regression, random forest, and a small feed-forward neural network (two hidden layers,
        64 and 32 units).
      </p>

      <table>
        <thead>
          <tr><th>k-mer</th><th>Logistic regression</th><th>Random forest</th><th>Neural network</th></tr>
        </thead>
        <tbody>
          <tr><td>k3</td><td>0.723</td><td>0.759</td><td>0.810</td></tr>
          <tr><td>k4</td><td>0.775</td><td>0.757</td><td>0.804</td></tr>
          <tr><td>k5</td><td>0.767</td><td>0.741</td><td><strong>0.820</strong></td></tr>
          <tr><td>k6</td><td>0.654</td><td>0.750</td><td>0.808</td></tr>
          <tr><td>k7</td><td>0.669</td><td>0.746</td><td>0.779</td></tr>
          <tr><td>k8</td><td>0.594</td><td>0.749</td><td>0.760</td></tr>
        </tbody>
      </table>
      <p style="margin-top: -1rem; font-size: 0.88rem; color: var(--ink-faint);">
        Matthews Correlation Coefficient by k-mer length and model architecture. The neural
        network wins at every k, peaking at k = 5.
      </p>

      <p>
        Five-mers hit a sweet spot: long enough to capture host-specific motifs, short enough to
        avoid the sparsity that creeps in as the feature space grows exponentially (4<sup>k</sup>
        dimensions). Past k = 5, performance degrades across every model, worst of all for
        logistic regression, which suggests the extra length adds noise faster than signal once
        you're past short local motifs.
      </p>

      <h2>Does it generalize to viruses it's never seen?</h2>
      <p>
        A model that only memorizes training-set families isn't useful for anything new. So we
        ran a leave-one-family-out test: hold out an entire virus family, train on the rest,
        then predict human-host compatibility on the excluded family. The strongest result was
        <em>Hepadnaviridae</em> (MCC = 0.828 at k = 6), the family that includes Hepatitis B,
        while vector-borne and zoonotic families like <em>Togaviridae</em> and
        <em>Rhabdoviridae</em> stayed near zero across every k-mer length. That's not a failure
        of the model so much as a biological finding: those families' genomic composition looks
        like it's shaped more by their arthropod or wildlife reservoirs than by any consistent
        human-adaptation signature.
      </p>

      <h2>What is the model actually looking at?</h2>
      <p>
        Raw k-mer frequency vectors barely separate human from non-human genomes under t-SNE, but
        the network's learned 32-dimensional embeddings do, cleanly enough to form distinct
        islands per virus family. Overlaying predicted probability on that embedding space turned
        up something we didn't expect: viruses with weak predicted human-adaptation
        (rabies, Eastern equine encephalitis) have dramatically higher human fatality rates, while
        viruses with strong predicted adaptation (HPV, human cytomegalovirus) are nearly always
        mild. The zoonotic middle ground, monkeypox, dengue, West Nile, sits exactly where you'd
        expect: transitional probability, epidemic rather than purely fatal.
      </p>

      <div class="callout">
        <span class="callout-label">Unexpected finding</span>
        <p>
          The model kept flagging human roseoloviruses (HHV-6A, HHV-6B, HHV-7) as non-human,
          despite them being common, mild human infections. Ablating individual k-mers traced the
          signal to fragments of the telomeric repeat <code>TTAGGG</code>, sequence roseoloviruses
          carry at their genome termini to integrate into host chromosome telomeres during
          latency. Almost no other human herpesvirus in the training set uses that persistence
          strategy, so the network had learned to associate telomeric motifs with non-human
          hosts. It wasn't wrong about the sequence pattern, it had just never seen this
          particular human trick before. Gallid alphaherpesvirus 2 (Marek's disease virus),
          which uses the same telomeric-integration strategy in chickens, clusters right next to
          the misclassified roseoloviruses in embedding space.
        </p>
      </div>

      <h2>Real-world test: SARS-CoV-2</h2>
      <p>
        None of the training data included coronaviruses. As a real-world stress test, we scored
        8,683 human SARS-CoV-2 genomes and 1,188 non-human betacoronavirus genomes with the
        trained classifier. Predicted human-adaptation probability separated the two groups
        cleanly (Mann-Whitney and Kolmogorov-Smirnov, both p &lt; 1&times;10<sup>-300</sup>;
        Cohen's d = 2.61), even though the model had never seen a coronavirus during training.
        Gene-level ablation on paired genomes, bat coronavirus RaTG13 (2013), Wuhan-Hu-1 (2019),
        and a 2024 human isolate, showed the human-adaptive signal concentrating in ORF1ab, ORF3a,
        E, M, and N as the lineage spent more time circulating in humans.
      </p>
      <p>
        We also tracked predicted human-adaptation probability across 8,683 SARS-CoV-2 genomes
        collected from December 2019 through January 2025, and found a small but statistically
        significant upward drift (p &lt; 0.0001) consistent with the virus continuing to
        accumulate human-adaptive signal well after the initial outbreak. That trend deserves its
        own interactive chart, one is planned for this page.
      </p>

      <h2>Where this goes next</h2>
      <p>
        The binary human / non-human framing simplifies a messier biological reality, and
        repository sampling bias means clinically important viruses are overrepresented. The
        roseolovirus result is also a good reminder that k-mer frequency alone can conflate
        genuinely different biological strategies that happen to leave similar sequence
        signatures. Next steps: expanding taxonomic coverage, testing alternative sequence
        vectorizations, and building out community infrastructure so the dataset can grow past
        this first release.
      </p>

      <div class="resource-links">
        <a class="btn btn-primary" href="https://doi.org/10.1093/ve/veag009" target="_blank" rel="noopener">Read the paper</a>
        <a class="btn btn-secondary" href="https://hiyata.github.io/host-virus_dataset/" target="_blank" rel="noopener">Interactive dataset explorer</a>
        <a class="btn btn-secondary" href="https://github.com/hiyata/host-virus-dataset" target="_blank" rel="noopener">GitHub</a>
        <a class="btn btn-secondary" href="https://huggingface.co/datasets/hiyata/Virus-Host-Genomes" target="_blank" rel="noopener">Dataset on Hugging Face</a>
        <a class="btn btn-secondary" href="https://huggingface.co/spaces/hiyata/HostClassifier" target="_blank" rel="noopener">Try the classifier</a>
      </div>

    </div>
  </div>
</article>
