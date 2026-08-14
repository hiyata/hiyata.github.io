---
layout: default
title: Does a Human-Adaptation Signal Learned in One Herpesvirus Genus Transfer to the Others?
category: virology
excerpt: A deep neural network trained only on Betaherpesvirus genomes correctly predicts human-host compatibility for Alpha- and Gammaherpesvirus genomes it never saw during training, 79% accuracy on a genuinely held-out genus.
presented_at: Lab Retreat Talk
permalink: /herpesvirus-generalization/
---

<article class="post-page">
  <div class="post-page-wrapper">
    <header class="post-page-header">
      <a class="post-page-back" href="{{ '/projects' | relative_url }}">&larr; Projects</a>
      <p class="post-page-kicker">Case Study &middot; In Progress</p>
      <h1 class="post-page-title">Can Betaherpesvirus Teach a Model to Recognize Human Alpha- and Gammaherpesviruses?</h1>
      <p class="post-page-meta">
        Alan Carbajo Jr., with Taylor Vensko and Dr. Phil Pellett &middot; Pellett Lab, Wayne State University
      </p>
    </header>

    <div class="post-page-content">

      <p>
        A genome is a low-dimensional record of everything a virus does inside a cell, entry,
        replication, persistence, immune evasion, compressed into four letters. The
        <a href="{{ '/virus-host-classifier' | relative_url }}">host-range classifier project</a>
        showed that a neural network can pull a human-adaptation signal out of that record using
        nothing but k-mer frequency. This follow-up asks a narrower, harder question: is that
        signal specific to the training data, or is it a real pattern that transfers across
        genuinely unseen viruses?
      </p>

      <p>
        <em>Orthoherpesviridae</em> is a good place to ask that question. It splits into three
        subfamilies, Alpha-, Beta-, and Gammaherpesvirinae, that diverged long ago and differ in
        cell tropism, latency strategy, and genome organization, but all share the family's core
        biology. If a model trained only on Betaherpesvirus genomes can still recognize human
        infection in Alpha- and Gammaherpesvirus genomes it has never seen, that's evidence the
        network learned something about human adaptation itself, not just about
        <em>Betaherpesvirinae</em>.
      </p>

      <div class="stat-strip">
        <div class="stat-strip-item">
          <span class="stat-strip-value">1,680</span>
          <span class="stat-strip-label">Orthoherpesviridae genomes, all subfamilies</span>
        </div>
        <div class="stat-strip-item">
          <span class="stat-strip-value">440</span>
          <span class="stat-strip-label">Betaherpesvirus genomes used for training, only</span>
        </div>
        <div class="stat-strip-item">
          <span class="stat-strip-value">1,220</span>
          <span class="stat-strip-label">Alpha- + Gammaherpesvirus genomes held out entirely</span>
        </div>
        <div class="stat-strip-item">
          <span class="stat-strip-value">79%</span>
          <span class="stat-strip-label">accuracy on that fully unseen genus split</span>
        </div>
      </div>

      <h2>A deliberately unfair test</h2>
      <p>
        We labeled every genome in <em>Orthoherpesviridae</em> human or non-human from NCBI host
        fields and taxonomy, then extracted 6-mer nucleotide frequencies exactly as in the
        host-range classifier. But instead of a random train/test split, the training set was
        restricted to <em>Betaherpesvirus</em> genomes only (n = 440), human cytomegalovirus,
        HHV-6, HHV-7 and their non-human relatives. Every <em>Alphaherpesvirus</em> (HSV-1, HSV-2,
        VZV) and <em>Gammaherpesvirus</em> (EBV, KSHV) genome, 1,220 sequences in total, was held
        out completely. The model never saw a single one during training.
      </p>

      <figure class="figure-wide">
        <img src="{{ '/assets/images/Design_HCMV_neural_network.webp' | relative_url }}" alt="Deep neural network architecture: Betaherpesvirus genomes for training, Alpha- and Gammaherpesvirus genomes for testing, three 1024-unit dense layers plus a 256-unit layer with normalization and dropout, output as human or non-human">
        <figcaption>Train/test split and architecture. Training data (blue) is Betaherpesvirus only; the test set (gray) is every Alpha- and Gammaherpesvirus genome in the dataset, none of which the network has seen.</figcaption>
      </figure>

      <p>
        The network itself is a straightforward feed-forward stack: three dense layers of 1,024
        units, then a 256-unit layer, each followed by batch normalization and dropout, feeding a
        two-class output. Simple architecture, deliberately hostile evaluation.
      </p>

      <h2>Watching the model learn, epoch by epoch</h2>
      <p>
        After every training epoch, we ran PCA on the model's learned embeddings for the full
        dataset, training and held-out genera together, and watched how the space reorganized.
        At epoch 1, human and non-human sequences from every subfamily are scattered together
        with no structure. By epoch 25, distinct clusters have formed, and critically, the
        separation shows up not just for the Betaherpesvirus training genomes but for the
        Alpha- and Gammaherpesvirus genomes the model was never trained on.
      </p>

      <figure class="figure-wide">
        <video src="{{ '/assets/videos/pca_embeddings_video_combined_hcmv_training_pca.webm' | relative_url }}" controls preload="metadata" playsinline></video>
        <figcaption>PCA of the model's learned embeddings across training epochs, colored by true and predicted host. Structure that starts as noise resolves into clusters that hold up even for genera the model never trained on.</figcaption>
      </figure>

      <h2>The result: it generalizes, and the baselines don't</h2>
      <p>
        On the held-out 1,220 Alpha- and Gammaherpesvirus genomes, the network reached 79%
        accuracy, with precision and recall balanced across both classes. That's the more
        important detail: it isn't winning by defaulting to the majority class.
      </p>

      <figure class="figure-wide">
        <img src="{{ '/assets/images/Human-nonhuman_HCMV_prediction.webp' | relative_url }}" alt="Comparison table: logistic regression 42% accuracy with 0.00 precision/recall/F1 on the human class, XGBoost 66% accuracy with 1.00 recall but only 0.32 recall on non-human, deep neural network 79% accuracy with balanced 0.78-0.79 F1 on both classes">
        <figcaption>Held-out performance on 1,220 Alpha- and Gammaherpesvirus genomes. Logistic regression collapses entirely on the human class (F1 = 0.00); XGBoost swings hard toward non-human; the deep network is the only one that generalizes to both classes.</figcaption>
      </figure>

      <p>
        Logistic regression is the most telling failure: 0.00 precision, recall, and F1 on the
        human class. It didn't just generalize poorly, it never learned a usable linear boundary
        for human-host signal outside the training genus at all. XGBoost does better overall
        (66% accuracy) but only by leaning hard on non-human predictions, recall on that class is
        1.00 while non-human recall is 0.32. The deep network is the only model that holds a
        genuinely balanced boundary across a genus it never trained on. This result held up
        across more than 300 architecture and hyperparameter configurations we tested before
        settling on the final design.
      </p>

      <h2>Looking inside a wrong answer</h2>
      <p>
        Aggregate accuracy hides individual failures, and those failures are often the more
        useful thing to look at. Below is the network's neuron activations for a single held-out
        genome, Cervid alphaherpesvirus 2 (a non-human virus infecting reindeer), propagating
        through each dense layer to a final prediction. The model calls it human. It's wrong, but
        watching where the activations diverge from a typical non-human pattern is exactly the
        kind of trace that turned up the telomeric-repeat story in the companion host-range
        classifier project.
      </p>

      <figure class="figure-wide">
        <video src="{{ '/assets/videos/neuron_activation_video.webm' | relative_url }}" controls preload="metadata" playsinline></video>
        <figcaption>Neuron activations across all four dense layers for Cervid alphaherpesvirus 2 (NC_075563.1), true label non-human, predicted human. Tracing individual misclassifications like this is how we plan to identify the specific sequence motifs the network is generalizing on.</figcaption>
      </figure>

      <div class="callout">
        <span class="callout-label">What this is building toward</span>
        <p>
          A model trained on one herpesvirus subfamily correctly reading human-adaptation signal
          in two subfamilies it never saw is evidence the signal is real, not an artifact of
          <em>Betaherpesvirinae</em> specifically. The open question is what the network actually
          converged on: are there sequence-level "grammar" rules for human compatibility that
          hold across an entire virus family, or even across families entirely? Untangling that,
          the same way ablation work traced HHV-6's misclassification to telomeric repeat motifs,
          is the current focus.
        </p>
      </div>

    </div>
  </div>
</article>
