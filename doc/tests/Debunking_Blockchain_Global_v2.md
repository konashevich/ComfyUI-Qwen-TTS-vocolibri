---
bibliography: project_acacia_refs.json
csl: style.csl
link-citations: true
lang: en-GB
---
# Debunking Blockchain Misconceptions: Why Public Permissionless Blockchains Are the Viable Path for Digital Payments and Tokenised Assets

Oleksii Konashevych, PhD
<oleksii@konashevych.com>

December 2025

---

## Table of Contents

- Abstract
- Summary
- 1. Introduction
- 2. The Blockchain: Architecture of Trust in an Open Network
- 3. Misconceptions and Barriers to Public Blockchain Adoption
- 4. Towards a Blockchain-Native Regulatory Architecture
- References

---

## Abstract

Permissioned distributed ledger technologies (DLT) have been widely promoted as the appropriate solution for governments and financial institutions seeking to implement digital payments and tokenised assets. This positioning rests upon fundamental misconceptions about public permissionless blockchains that have permeated academic literature and policy discourse for over a decade. This paper systematically debunks these misconceptions and demonstrates that permissioned DLTs represent centralised systems masquerading as decentralised infrastructure—offering neither the security nor the reliability of true blockchains. Through comparative analysis of security architectures, governance models, and economic incentive structures, it is established that public permissionless blockchains such as Bitcoin and Ethereum provide demonstrably superior infrastructure for digital financial applications. The paper addresses entrenched objections to the use of such blockchains and presents a practical framework for implementing cerntral bank‑issued or authorised digital currencies and regulated financial applications on public blockchains, whilst maintaining full regulatory control and jurisdictional reach. The evidence compels a fundamental reassessment: embracing public blockchain infrastructure is not merely an option—it is the ultimate technically sound and economically rational path forward.

---

## Summary

### 1. Introduction and Explanatory Note

Permissioned ledger technologies have been positioned as the solution for governments and major institutional players. This class of technologies was created to address perceived problems that supposedly prevent the use of open, public blockchain networks. The reality is inverted: public blockchain risks are overstated and manageable, whilst permissioned systems exhibit the very security weaknesses they purport to avoid. Moreover, whilst public networks are actively developing, permissioned systems are finding a far narrower economic application and are significantly more modest in terms of technological innovation (see Section 1).

In this paper, the word "blockchain" is used in its original sense. Whenever the term blockchain appears, it refers exclusively to public permissionless networks. Permissioned ledgers are not blockchains—a distinction that will be addressed separately.

### 2. Why This Matters

Deeply rooted misconceptions regarding both types of technologies need to be addressed for two reasons:

1. The non-application of blockchain technologies entails a loss of benefits that are still poorly understood.
2. The application of permissioned distributed ledger technologies (DLT) entails risks. There has been a conflation of concepts, where the beneficial properties of blockchains are transferred to permissioned ledgers (and thus also called permissioned blockchains). In the best-case scenario, this will not lead to the transformative consequences and significant economic advantages expected from this technology. In the worst-case scenario, misled policymakers and officials will foster implementation of unreliable technology that will eventually explode like a time‑bomb (see Section 1.1).

### 3. The Fundamental Flaw: Centralisation Masquerading as Decentralisation

The terms "permissioned" and "private" imply the presence of an administrative component in the network. This naturally constrains the network's ability to scale. It is impossible to find a permissioned system that operates, say, twenty-five to eighty thousand nodes like in Bitcoin. Consequently, such a network cannot achieve a level of data security and cyber protection comparable to blockchain. Thus, such a network is not immutable and is a variant of centralised technology ("permissioned" is a euphemism for centralised). The security of the system, as in any other centralised networks, is achieved through its closed nature, and the administrative component regulating node access to the network constitutes a single point of failure (see Section 2.5).

Not every chain of blocks is the blockchain. The method of building chains of blocks was invented in 1991, and its purpose is not data protection, but rather a method of verifying data against tampering. What makes a chain of blocks the blockchain is open competitive consensus. It allows anyone to participate in block creation (e.g., "mining"), which is essentially a method of data synchronisation, whilst the mining reward is an economic incentive for independent operators to provide their computational resources for public use.

### 4. The Reliability Paradox: Why "Unreliable" Public Blockchains Outperform Everything Else

There is a widespread belief that blockchain's open competitive consensus poses a threat to stability. Yet relying on this supposedly unreliable mechanism, networks like Bitcoin and Ethereum have grown to such a scale that they have achieved practical ledger immutability, invulnerability to DDoS attacks, 51% attacks, and other existential network threats. Bitcoin is the only example of a public network (not just blockchain, but any open public system) that has operated without failure for nearly 17 years with 100% uptime. Bitcoin is the most reliable digital data repository ever created by humankind (see Sections 1.1, 3.2.1, and 3.2.2).

The open competitive model of blockchain operation, where mining serves as the economic driver, results in a completely self-organising network that requires no effort from individual participants for its development and management. Permissioned ledger networks, conversely, require not only an administrator for node authorisation and transaction censorship but also an owner from an infrastructure perspective. Some infrastructure creation and management tasks can be delegated to participants within such a closed network, but an adequate economic model is essential in any case (see Section 2.4).

### 5. The Governance and Legitimacy Challenge

When government agencies participate in permissioned systems, questions of legitimacy may arise if law mandates that such agencies manage infrastructure for, e.g., a registry or government service. Delegating such powers may require new legislation. For example, laws were passed in four Australian states to transfer land registries to private companies under concession management (see Section 3.3.3).

For the same reason—vulnerability of centralised systems to penetration and alteration—public registries may face geographical location requirements, since governments may be unable to ensure physical or jurisdictional control over data centres where applications and their data are processed if located on foreign territory.

The situation with blockchain is different. Storing personal data on-chain (beyond the transactions themselves) is expensive and unnecessary; such data should still be held in closed, centralised systems under jurisdiction and control, anchored to the blockchain. Meanwhile, territorial requirements for blockchain are simply irrelevant, as there is no adequate threat of data compromise. Indeed, ledger immutability is the primary reason for using blockchain—it enables the creation of public applications without the need to manage infrastructure, which in turn proves orders of magnitude more reliable than even infrastructure locked away deep within some organisation's fortified data centre (see Section 3.2.3).

A commercial permissioned ledger network uniting certain market participants may constitute contracts, arrangements, or concerted practices that substantially lessen competition, raising concerns under competition law frameworks such as Australia's Competition and Consumer Act.

### 6. The Architecture Question: Who Controls What?

There is a substantial difference in the application of permissioned ledgers versus blockchains, as well as in the architecture of applications built on these systems. A common question arises: "Who will run the nodes?" In permissioned ledgers, it is critical that nodes be verified, as their actions can influence the business logic of the applications themselves. As a centralised system, no matter how complicated the order of data modification may be, if such a possibility genuinely exists, then the nodes of such a system essentially act as both infrastructure owners and owners of the applications running there.

In blockchain, conversely, nodes engage in mining—synchronising the distributed digital repository—but remain separate from the internal business logic of applications operating in that digital space. The task of nodes in such a network is simply to provide infrastructure for applications, whilst cryptocurrency serves as compensation for a node providing its computational capacity for public use through the mechanism of block rewards and transaction fees. Just as an application hosted in traditional cloud infrastructure, say Amazon or Azure, is not identified with the cloud itself, similarly in blockchain, smart contract business logic (essentially the application) is separated from consensus. Only in blockchain does this separation reach its maximum—nodes have no technical means to control processes within individual decentralised applications (smart contracts) (see Section 3.1.1).

### 7. The "Trustless" Misconception

There is a widespread misconception regarding the word "trustless". Its meaning is limited to the fact that there is no trusted administrator in the network and does not apply to the applications themselves. Although there are numerous examples where smart contracts themselves are also trustless (a unique capability that simply cannot exist in centralised systems)—for instance, "DEX" decentralised exchanges—applications (smart contracts) for government administration tasks (examples: CBDC or land registry, if such is created) or in regulated spheres (traditional finance) can and should have an administrator possessing exclusive full authority within the scope of such an application. From a practical standpoint, this means the ability to invalidate any tokens, transactions, and addresses (for example, burn tokens and/or reissue new ones, block addresses, etc.) (see Section 3.1.2).

This issue also relates to a persistent misconception according to which ledger immutability makes its use impossible under real legal conditions. Problems are raised such as errors or crimes (e.g., theft of coins), legal disputes, or even simple loss of keys potentially leading to legal deadlock. However, these issues concern cryptocurrency as a separate type of native and singular application operating at the consensus level. When cryptocurrency in relation to smart contracts serves merely as a payment system for network node services (e.g., "gas fee") for infrastructure use, these problems are irrelevant. The "immutability problem" is contrived and resolved through adequate smart contract architecture, which will have a managing administrator with full legal and technical decision-making authority, without the need to retrospectively alter the ledger (see Section 3.1.3).

### 8. How the Real World Actually Works

In the real world, data in public registries (e.g., land registry, ledger) are not changed retrospectively. All required changes—whether correcting errors, executing court decisions, or otherwise—are appended as new entries. In this sense, blockchain is the ultimate solution, as it not only preserves a data archive but is chronologically immutable. This enables any updates in a smart contract whilst referring only to the latest entry as a single, consistent source of truth (see Section 3.1.3).

### 9. Government Crypto Holdings and the Use of Blockchain

Governments around the world hold large quantities of crypto-assets (mainly seized from criminal activity) and continue to acquire them. A question arises: why does not government sell these assets if it fears their unreliability? On the contrary, some countries are forming crypto reserves. If they trust this technology, then why not use public blockchains as an infrastructure solution? (see Section 3.4).

### 10. Risk Management, Not Risk Avoidance

All known threats and risks of blockchain are either localised or manageable. There is not a single problem in blockchain that cannot be adequately managed; there are only misconceptions about it. One of the main frequently mentioned problems is the 51% attack. However, first, for networks like Bitcoin, Ethereum, and several others, this threat is in the past. Second, the problem itself is not properly understood. Such an attack in Proof-of-Work consensus—a percentage above 50%, say 1%—represents a 51 against 49 chances of producing the next block faster than the rest—a chance, not a guarantee. And even securing it, an attacker has no ability to change transaction history after block confirmation. The nature of harm such an attack can inflict will be limited. Building up control could potentially create a greater threat to the network, but this is an extraordinarily difficult task. So difficult that we see Bitcoin operating without failure since 2008. Naive Proof-of-Stake consensus, where possibilities for deep 50+1% attacks aimed at rewriting block history, are also now in the past, e.g., the Casper protocol in Ethereum is resistant to this attack (see Section 3.2.1).

And third, reasonable application of blockchain technology should assume, as with any technology, the existence of a contingency plan. The logic that "someone might gain control over the network, therefore it cannot be used" is simply flawed. The same could be said of any technology. Risks must be managed not avoided (see Section 3.2).

For example, there exists a protocol for alienating a compromised blockchain from a blockchain-based registry, and together with backup and data migration protocols, further discussed in this paper it enables the ability, if necessary, to transfer user applications seamlessly to end users, since the same private key can work in smart contracts on different blockchains (see Section 4.6).

### 11. The Hard Fork Myth

The second significant network threat is conventionally considered to be hard forks. The history of The DAO that led to the Ethereum network split, as well as the retrospective rescue of stolen coins, supposedly serves as a warning to governments.

First, a hard fork is essentially a new network. In The DAO split situation, there was no coercion to transfer to another network. Transitioning to another network required active, voluntary action by each individual network participant to transfer their node to the new network. Simply put, it was honest market competition where participants and users acted consciously, without deception or coercion. If a node operator did not wish to install new software, it simply remained in the original network, which subsequently received the name Ethereum Classic (still operating today).[@5PIBKG29] More simply, if a user relies on an application, it remains unchanged on the original chain, as does all associated data. However, the central point is not merely continuity: the protocol proposed above, analogous to the strategy for a 51% attack, permits the transfer of an application, comparable to an entity migrating from one cloud service provider, such as Amazon, to another, such as Microsoft Azure. Thus, even in this scenario, the discussion concerns risk management rather than a fundamental limitation (see Section 3.1.4).

### 12. Scalability Through Multi-Chain Architecture

The throughput problem of an individual blockchain is contrived, since there is no necessity to exclusively use only one blockchain. The same protocol discussed in the paper is built around the idea of linking blockchains, whose aggregate throughput can be greater than any single centralised system (see Section 3.2.4).

Cryptocurrency volatility, often mentioned as a blockchain problem, as stated above, is a localised problem since cryptocurrency is needed as payment for "gas". Payment is formed based on open competition, which is inherently fair and may prove better for the market than cartel collusion in permissioned ledgers. The volatility problem is also not empirically confirmed. Spikes in smart contract execution fees have not halted DeFi development; on the contrary, they led to the emergence of more competitive systems: Solana, Tron, BNB Chain, and others (see Section 3.3.1). The same can be said about the privacy problem. Ledger publicity has not prevented its wide application, and technologies such as zero-knowledge proofs have addressed the need in situations where publicity is undesirable (see Section 3.2.3).

### 13. Addressing Ethical and Legal Concerns

Government may be concerned about miners/validators (block producers) operating from sanctioned jurisdictions or controlled by entities deemed ethically unacceptable. The concern is that such validators would earn transaction fees from processing government application transactions, potentially circumventing sanctions policy.

This problem is addressed through a two-tier enforcement approach. First, governments establish authorised transaction submission channels—operated relayers that bypass the public mempool and route transactions exclusively to a whitelisted network of compliant validators operating in acceptable jurisdictions. Sanctioned validators never observe these transactions and earn no fees from government applications. Second, the smart contract itself enforces a validator whitelist by checking the block producer's address; transactions processed by unauthorised validators are not settled, meaning the token will not be transferred. This on-chain enforcement ensures that even if a user attempts to circumvent the official channel by broadcasting directly to the public mempool, the transaction fails and the user is penalised for non-compliance by paying gas fees for a failed transaction. While the sanctioned validator may collect this gas fee, the transaction itself achieves nothing—the regulated assets are not transferred. The combination of private routing and on-chain validation provides robust control without compromising the decentralisation or security of the underlying public blockchain (see Section 3.3.2).

### 14. The Innovation Dividend

The application of public blockchains holds tremendous potential. As we see, the closed nature of permissioned systems does not contribute to their rapid development and implementation. Conversely, the open nature of blockchain systems has made blockchain ecosystems epicentres of technological and economic innovation, with total capitalisation reaching $4 trillion USD. Everything we know about blockchain, from the moment Satoshi Nakamoto's paper was published to today, is the result of open collaboration worldwide. A government deciding in favour of admitting blockchains into regulated spheres such as dollar circulation and finance acquires all this innovative potential to its benefit (see Section 1.1).

Moreover, public networks are a source of liquidity that already exists. Each permissioned ledger, conversely, needs to create its own ecosystem and attract liquidity from scratch. The enormous liquidity of public blockchains merely needs to be attracted and competently harnessed through policies for admitting clean cryptocurrencies into the regulated perimeter of state jurisdiction on blockchain.

### 15. Building Jurisdiction on Blockchain

The future of the Digital Economy and functionality of regulated Decentralised Finance (DeFi) rely on a paradigm shift towards on-chain regulation. Traditional regulatory models, such as paper licences and off-chain registries, create bottlenecks and single points of failure when applied to digital markets. For a programmable economy to function—where exchange is instant and intermediary-free—all components of the transaction must exist within the same technological environment.

A regulated digital economy rests on three pillars: the Digital Token representing property rights, Digital Money, and Digital Identity. These pillars require a permanent formwork of on-chain governance—jurisdiction on blockchain—where regulatory authorisation is actionable code, not just legal text.

This jurisdiction can be built using the Cross-Blockchain Protocol of Public Registries that relies on an abstraction layer, an overlaid protocol, embedded in user wallets. This allows the government to build a multi-chain regulated perimeter utilising existing, highly secure public blockchains, such as Bitcoin and Ethereum, as trusted infrastructure. Crucially, this architecture enables seamless cross-chain transactions without the need for third-party orchestrators or intermediaries, as the validity of assets and identities is verified locally by the protocol against on-chain public registries.

Consequently, the state's mission shifts from acting as a central operator to an infrastructure enabler. The primary governmental tasks include developing and maintaining the technical protocol and its updates, monitoring blockchain reliability through measures such as hash rate, and curating the bundle of authorised blockchains. Furthermore, the state is responsible for maintaining root addresses and public registries of authorised entities, ensuring data backup, and managing application migration if a network becomes compromised. Finally, the government protects fair competition in the mining sector, reflecting its role in supporting ecosystem stability.

### 16. The Ultimate Question

This paper does not examine the question of who will administer the digital dollar—whether it be the central bank or private financial institutions. What matters is critically understanding that not only can this be done on a public blockchain, but it is the ultimate path forward, because blockchains have proven their reliability. They are here to stay, and the question is which government will be first to harness the enormous potential of global cooperation and extract maximum benefit for its economy (see Section 4.9).

To look at the blockchains and act as if they are non-existent is a political blunder, to say the least. The choice is clear: embrace the proven, reliable, innovative infrastructure of public blockchains, or persist with the expensive, centralised, and ultimately futile experiment of permissioned ledgers. History will not look kindly on those who chose the latter.

---

The topics summarised above are examined in detail in the full paper.

---

## 1. Introduction

The trajectory of distributed ledger technology (DLT) adoption over the past decade presents a striking paradox. Whilst permissioned DLT systems such as Hyperledger Fabric[@DRX688QB] and R3 Corda[@4SVQVNCR] were championed by academic institutions, major consulting firms, and policy advisers as the appropriate infrastructure for governments and financial institutions, the empirical evidence reveals a profoundly different reality. Despite inflated expectations, substantial investment, and institutional backing, permissioned DLT implementations have largely stalled in proof-of-concept limbo, with alarming failure rates that belie the confident projections of their proponents.[@9IWPKJCW; @J73S9D9M]

Meanwhile, public permissionless blockchains—silently dismissed by many as unsuitable for serious financial applications—have emerged as the genuine epicentres of technological innovation and economic activity. With a combined market capitalisation exceeding $4 trillion USD in October 2025 and demonstrable reliability spanning nearly 17 years of continuous operation, networks such as Bitcoin and Ethereum have delivered what permissioned systems promised but failed to achieve: secure, resilient, and scalable infrastructure for digital financial applications.

This paper systematically dismantles the misconceptions that have dominated blockchain discourse and policy formation, presenting compelling empirical evidence that demands a fundamental reassessment of technology choices for digital payments and tokenised assets. The stakes are high: continuing down the path of permissioned DLT represents not merely a suboptimal choice, but an expensive, risky, and ultimately futile endeavour that diverts resources from the only proven solution—public permissionless blockchain infrastructure.

The core thesis of this research is straightforward. Permissioned DLT is a type of centralised system that does not possess the perceived 'blockchain' qualities and properties regarding data security; its benefits in the public sector and regulated markets are questionable, and its risks are higher compared to genuine blockchains. In contrast, public blockchains ensure ultimate data protection. The perceived barriers and disadvantages of this technology are false. This is the right choice that will secure progress into the future, and a government that recognises this stands to gain enormous benefits.

### 1.1 Background and Context

#### The Rise of Permissioned DLT Hype (2015–2018)

The period from 2015 to 2018 witnessed an unprecedented wave of enthusiasm for permissioned distributed ledger technologies. Major consulting firms including Deloitte, PwC, and KPMG published numerous reports extolling the virtues of "enterprise blockchain" solutions.[@67P34B7Q] Academic institutions produced a number of research papers conceptualising permissioned DLT whilst systematically ignoring public blockchains for institutional applications.[@BBQ6KENU] Technology vendors, led by initiatives such as the Linux Foundation's Hyperledger project (launched in 2015) and R3's Corda platform (announced in 2016), positioned their permissioned systems as the appropriate answer to perceived limitations of public blockchains.

The narrative was seemingly rational: permissioned systems would deliver blockchain's promised benefits whilst addressing concerns about scalability, privacy, regulatory control, and governance that supposedly made public blockchains unsuitable for financial institutions and government agencies. This positioning enjoyed widespread acceptance across policy circles, with central banks, financial regulators, and government departments worldwide initiating exploratory projects based on permissioned DLT architectures.

Crucially, this period saw a substitution of concepts take hold. The term "blockchain" began to be used as a generic umbrella term, with its desirable properties of immutability and security being conflated with and attributed to permissioned DLT. This conceptual confusion was critical to the hype, as it allowed permissioned systems to be marketed with the perceived benefits of true blockchains, whilst appearing to mitigate their perceived risks.

Seminal publications by the World Economic Forum reinforced this trajectory: the 2015 Deep Shift report forecast "10% of global gross domestic product (GDP) stored on blockchain technology" by 2027,[@CEP99IRR] the 2016 The Future of Financial Infrastructure report mapped priority financial services use cases and operating models for distributed ledgers,[@ADFZRVGW] and the 2018 "Blockchain Beyond the Hype" paper provided a practical decision framework used by business leaders and officials assessing blockchain initiatives.[@TJ7J2NMP]

Gartner Inc., the influential technology research and advisory firm, added blockchain to its annual Hype Cycle in 2016, rapidly elevating it towards the "Peak of Inflated Expectations" by 2017–2018.[@NZRGR7JV] The technology garnered extraordinary attention from C-suite executives, with surveys indicating that a majority of financial institutions were exploring or planning blockchain implementations.[@WZ9BAKND] Major banks formed consortia, governments announced pilot programmes, and technology budgets were allocated to what appeared to be the next transformative wave of digital infrastructure.

The academic literature of this period reflects this enthusiasm. Papers proliferated discussing use cases for permissioned blockchains in supply chain management, trade finance, healthcare records, and government services. The conceptual frameworks developed during this period established what would become entrenched assumptions: that permissioned systems were necessary for enterprise adoption, that public blockchains were too volatile and uncontrollable for regulated applications, and that "blockchain technology" could be cleanly separated from the public networks where it originated.[@4K5JFPGU]

#### The Empirical Reality: Failure to Launch (2019–Present)

By 2019, the empirical evidence began telling a starkly different story. Gartner's Hype Cycle for that year placed blockchain technology firmly in the "Trough of Disillusionment"—a dramatic fall from the lofty expectations of just two years prior.[@AW65B8ZH] This shift reflected an uncomfortable reality emerging from the data: permissioned DLT projects were failing to progress beyond pilot stages at alarming rates.

The most authoritative quantification of this failure comes from the University of Cambridge Centre for Alternative Finance's 2nd Global Enterprise Blockchain Benchmarking Study (2019).[@8U9RFBII] This comprehensive research, surveying 160 organisations—including start-ups, established companies, central banks, and public-sector institutions from 49 countries—revealed a striking gap between activity and achievement. Of these 160 organisations actively engaged in enterprise blockchain development, only a fraction had entered production. Research indicates that success rates for enterprise blockchain projects are exceptionally low, with some estimates citing rates as low as 3-5 per cent, with the vast majority of initiatives remaining stuck in pilot or proof-of-concept stages despite years of development effort and substantial investment.

Even more damning, a Gartner survey of blockchain service providers reported in 2020 that only 14% of enterprise blockchain projects had transitioned to production, up from 5% in 2019 (as cited in Tracey & Ruamsook).[@8R8RVHCW] This means that 86% of enterprise blockchain initiatives failed to scale beyond experimental phases—a failure rate that would be considered catastrophic in any technology domain. To contextualise this figure: if 86% of cloud computing migrations or ERP implementations failed, the technology would be immediately abandoned. High‑profile outcomes in subsequent years reinforced this picture, including the shutdown of the IBM–Maersk TradeLens permissioned platform in 2022[@2JNA768T] and the cancellation/reset of the ASX CHESS replacement based on distributed ledger technology in 2022–2023.[@IMQVDZP6] In the first case, Maersk cited insufficient industry collaboration and a lack of commercial viability; in the second, ASX halted the DLT‑based replacement following an independent review and subsequently reset the programme toward a staged, non‑DLT architecture. The independent review identified significant challenges with the solution design and its ability to meet ASX's requirements.[@IMQVDZP6]

Further evidence of the reality gap emerged from CIO surveys. Research conducted in 2019 found that only 5% of Chief Information Officers assessed blockchain technology as ready for implementation in financial services.[@7M3SFRKW] This represents an extraordinary vote of no confidence from the very executives responsible for technology adoption decisions—95% of CIOs remained unconvinced despite years of vendor promises and consultant advocacy.

Academic research examining actual implementation outcomes paints an equally sobering picture. A 2023 study explicitly addressing the challenge of "moving beyond proof-of-concept and pilots to mainstream" noted "alarming failure rates" in enterprise blockchain applications.[@UZZUBDCQ] Research on blockchain adoption barriers documented that projects frequently discontinue after pilot phases,[@SWU5SBWA] whilst multiple studies characterised the gap between expectations and reality using terms such as "hype versus reality," "from hype to reality,"[@VRZCSXBQ] "hype-based adoption to implementation realities,"[@MGCNJSWW] and "beyond the hype."[@9TVSXC4M]

The reasons for these failures are well-documented in the literature. Research identified persistent challenges including excessive cost and complexity,[@7EVP9WVB] fundamental interoperability problems,[@59ANQF4D] security vulnerabilities inherent to centralised architectures,[@8F2H8HIW] and the absence of viable economic models to sustain network operations.[@ZKU6MJG9] Critically, multiple studies concluded that permissioned systems "become more centralised" in practice,[@8F2H8HIW] defeating the supposed purpose of adopting distributed ledger technology in the first place.

Research on blockchain project abandonment revealed high discontinuation rates. A 2019 study examining blockchain projects supporting open science found that after filtering for active projects (defined as activity within one year), only 60 projects remained from a substantially larger initial set, indicating significant attrition.[@KH6FEAMB] Analysis of blockchain consortia noted that permissioned initiatives "failed to garner" significant adoption despite years of development effort.[@ATFI4RM4]

Perhaps most tellingly, multiple researchers noted that "empirical studies are very few" examining actual permissioned DLT implementations,[@8CJB4B7Q] and that there exist "limited studies that analyse" real-world applications.[@8CJB4B7Q] This scarcity of empirical validation stands in stark contrast to the abundance of conceptual frameworks and theoretical use cases that dominated the literature during the hype phase. The implication is clear: there simply are not enough successful implementations to study.

#### The Contrasting Reality: Public Blockchains as Innovation Epicentres

Whilst permissioned DLT initiatives languished in proof-of-concept purgatory, public permissionless blockchains experienced explosive growth in technological sophistication, economic activity, and real-world adoption. This divergence represents one of the most significant misassessments in recent technology policy history.

Bitcoin, launched in 2009, has operated continuously for nearly 17 years without a single hour of downtime—100% uptime across its entire operational history.[@WKUHVJI9] No permissioned DLT system can claim comparable reliability. No centralised system operated by any corporation or government has achieved this level of operational resilience. Bitcoin represents the most reliable digital data repository ever created by humankind, a fact that stands in stark contrast to characterisations of public blockchains as "unreliable" or "unsuitable" for critical applications.

Ethereum, launched in 2015, has catalysed an entire ecosystem of decentralised applications (dApps) and decentralised finance (DeFi) protocols. As of October 2025, the DeFi ecosystem built on Ethereum and other public blockchains manages over $100 billion USD in total value locked (TVL).[@MS5RQG69] This represents real economic activity—not pilot programmes or proofs-of-concept, but actual financial services processing billions of dollars in daily transaction volume. Decentralised exchanges such as Uniswap process trading volumes comparable to mid-sized centralised exchanges, all executed through immutable smart contracts without intermediaries.

The pace of innovation on public blockchains has been extraordinary. Layer 2 scaling solutions such as Polygon, Arbitrum, and Optimism have achieved transaction throughput exceeding thousands of transactions per second whilst maintaining security guarantees inherited from Ethereum's base level.[@8QZ3XSGW] Zero-knowledge proof technologies, initially theoretical constructs, have been implemented in production systems enabling privacy-preserving transactions.[@KENNIGD2] Cross-chain bridges and interoperability protocols have created an interconnected ecosystem where assets and data flow seamlessly across multiple blockchain networks.[@WVWQDPQG]

Public blockchains have also proven remarkably adaptable to institutional requirements whilst maintaining their core properties. Ethereum's successful transition from Proof-of-Work to Proof-of-Stake consensus in 2022—coordinating a network upgrade across tens of thousands of independent validators without downtime—demonstrated governance capabilities that permissioned systems, ironically, have struggled to achieve.[@D7HWNP3Z] The implementation of EIP-1559, which fundamentally restructured Ethereum's fee market, showed that public blockchains can implement sophisticated economic mechanisms more effectively than the supposedly "manageable" permissioned alternatives.

The combined market capitalisation of public blockchain networks exceeds $4 trillion USD as of October 2025.[@QF72E33T] This represents real economic value—capital deployed by rational actors making investment decisions based on technological merit and utility. By comparison, the aggregate investment in permissioned DLT systems, whilst difficult to quantify precisely, has yielded vanishingly little productive economic activity relative to the capital deployed.

Critically, innovation on public blockchains occurs through open-source collaboration involving thousands of developers worldwide. Each breakthrough—whether in consensus mechanisms, cryptographic techniques, scaling solutions, or application architectures—immediately becomes available for others to build upon. This stands in stark contrast to the permissioned DLT industry, which has failed to serve as a source of technological innovation; indeed, virtually all significant advancements have originated from the open Web3 sector. Moreover, even where isolated technological novelties are realised, they can remain sequestered within closed environments, failing to contribute to the general benefit of the industry. This reinforces the key argument for governments and major financial institutions: blockchain technologies, by virtue of their openness—both in source code and network architecture—have become self-sustaining innovation epicentres, continuously paving the way for the future.

### 1.2 The Persistence of Misconceptions

The empirical evidence presented above raises a fundamental question: if permissioned DLT systems have demonstrably failed to deliver on their promises whilst public blockchains have proven themselves as reliable, innovative, and economically significant infrastructure, why do misconceptions favouring permissioned approaches persist so tenaciously in policy and institutional circles?

At the same time, a substitution of concepts has taken hold. "Blockchain" is treated as an umbrella term that somehow encompasses permissioned DLT. In academic and policy writing, the word "blockchain" is used arbitrarily—either to mean any chain-of-blocks data structure (not every chain of blocks is the blockchain), or, worse, as a synonym for permissioned DLT. This linguistic imprecision contaminates technology selection: policy-makers routinely impute to permissioned ledgers the properties that only blockchains possess—reliability, immutability, and adversarial security. Section 2.1 sets out the defining characteristics of true blockchains; Section 2.2 explains why permissioned DLT, notwithstanding its block-chaining, remains centralised infrastructure and therefore lacks those properties.[@BBQ6KENU; @UJPAXCD4; @8F2H8HIW; @X4ZJBGZR]

#### The Self-Reinforcing Nature of Misconceptions in Academic Literature

A primary factor is the self-reinforcing nature of misconceptions embedded in academic literature. The period from 2015 to 2018 saw a proliferation of academic papers that conceptualised permissioned DLT systems whilst systematically avoiding (explicitly or more often silently) public blockchains for institutional applications.[@BBQ6KENU] These papers established a conceptual framework and vocabulary that subsequent researchers built upon, creating a cascade of derivative work that amplified initial misconceptions rather than subjecting them to empirical validation.

Research examining this phenomenon identified that many academic papers discussing blockchain adoption barriers and challenges simply assumed that permissioned systems were the appropriate choice for enterprises and governments, then proceeded to analyse implementation obstacles without questioning the fundamental technology selection itself.[@BBQ6KENU] This created a literature where the central question—whether permissioned DLT is actually superior to public blockchains for institutional applications—was treated as settled rather than subjected to rigorous comparative analysis.

Large language models trained on this corpus of academic literature have inherited and amplified these misconceptions. When asked about blockchain applications for government or financial institutions, AI systems such as ChatGPT, Claude, and Gemini frequently recommend permissioned solutions, citing the very papers that embedded misconceptions in the training data.[@UJPAXCD4] This creates a feedback loop where misconceptions not only persist but become increasingly difficult to dislodge, as they appear validated by apparent consensus in the literature.

#### Cognitive Biases and Institutional Inertia

Several cognitive biases contribute to misconception persistence despite contradictory evidence. The sunk cost fallacy operates powerfully: organisations that invested substantial resources in permissioned DLT pilots face psychological pressure to justify those investments rather than acknowledge failure.[@NZRGR7JV] The appeal to authority bias leads policymakers to trust recommendations from major consulting firms and established technology vendors, even when empirical outcomes contradict their projections.[@TJ7J2NMP]

Status quo bias reinforces existing conceptual frameworks. The notion that governments and financial institutions require "permission" and "control" over their infrastructure appears intuitively reasonable to institutional decision-makers accustomed to centralised systems. Public permissionless blockchains, by contrast, require a conceptual leap: embracing infrastructure that no single entity controls but that is paradoxically more reliable and secure precisely because of that property. This counter-intuitive reality proves difficult for traditionally-minded institutions to accept.

Research on blockchain adoption identified "lack of understanding" as a fundamental barrier to appropriate technology selection.[@WZ9BAKND] This manifests not merely as insufficient technical knowledge, but as misconceptions about fundamental properties. Many institutional decision-makers genuinely believe that public blockchains are "unreliable," "uncontrollable," or "unsuitable for regulated applications"—beliefs that are factually incorrect but that shape technology choices nonetheless.

#### The Consultant-Vendor Complex

The persistence of permissioned DLT advocacy despite empirical failure is partially explained by economic incentives within the technology consulting and vendor ecosystem. Major consulting firms including Deloitte, PwC, KPMG, and Accenture have built substantial practices around "enterprise blockchain" implementations.[@67P34B7Q] These firms generate revenue from lengthy consulting engagements, custom development projects, and ongoing maintenance contracts—business models that thrive on complexity and proprietary solutions.

Public blockchains, by contrast, represent commoditised infrastructure available to anyone. They cannot be sold through lengthy consulting engagements or locked into proprietary platforms. The economic incentive structure favours complexity over simplicity, closed systems over open infrastructure. As Upton Sinclair observed, "It is difficult to get a man to understand something when his salary depends on his not understanding it."[@IX65VN49]

Technology vendors such as IBM (Hyperledger) and R3 (Corda) have similar incentives. These companies invested heavily in developing proprietary permissioned platforms and building partner ecosystems around them. Acknowledging that public blockchains represent superior infrastructure would require abandoning those investments and fundamentally restructuring their business models. The result is persistent advocacy for permissioned solutions despite mounting evidence of their inadequacy.

Research examining this dynamic noted that consulting reports and vendor materials consistently emphasised theoretical benefits of permissioned systems whilst minimising or ignoring implementation failures.[@EH8VUUBT] Multiple studies characterised industry discourse as prioritising "use cases" and conceptual possibilities over empirical validation of actual deployments.[@9TVSXC4M]

#### Regulatory Conservatism and Risk Aversion

Regulatory bodies and government agencies exhibit understandable conservatism regarding new technologies. The characterisation of public blockchains as "risky" or "unproven"—despite nearly 17 years of operational evidence to the contrary—provides convenient justification for regulatory caution. Conversely, permissioned systems, despite their demonstrated failures, are perceived as "safer" because they appear to maintain traditional control structures.

This perception is precisely backwards. Research examining security properties of permissioned versus public blockchains consistently found that permissioned systems "become more centralised" in practice,[@8F2H8HIW] exhibiting the same security vulnerabilities as traditional centralised databases whilst adding complexity without corresponding benefits.[@X4ZJBGZR] Public blockchains, by contrast, achieve security through radical decentralisation—a property that is counter-intuitive but empirically validated across billions of transactions and thousands of node operators over extended timeframes.

The regulatory mindset often confuses risk avoidance with risk management. The logic that "public blockchains might be attacked or fork, therefore they cannot be used" is fundamentally flawed. The same reasoning would prohibit use of the internet, cloud computing, or any technology with non-zero risk. As further shown, all known threats to public blockchains—51% attacks, hard forks, throughput limitations—are manageable through appropriate architectural choices and contingency planning. The relevant question is not whether risks exist, but whether they can be adequately managed relative to alternatives.

#### The "Not Invented Here" Syndrome

Institutional psychology exhibits strong preferences for solutions that organisations can claim to "own" or "control." Public blockchains, by definition, cannot be owned or controlled by any single entity—this is their strength, not their weakness. Yet this property triggers the "not invented here" syndrome in government agencies and large corporations, which prefer custom-built solutions over shared infrastructure, even when the shared infrastructure is demonstrably superior.

Research on enterprise blockchain adoption identified that organisations often initiated permissioned DLT projects to "benefit from the hype surrounding open blockchain" whilst maintaining traditional control structures.[@4K5JFPGU] This represents a fundamental category error: attempting to extract blockchain's benefits whilst negating the core property (permissionless decentralisation) that generates those benefits.

The correct analogy is instructive: no organisation today insists on building its own internet or demanding "permissioned HTTP." The internet's value derives precisely from its permissionless, globally accessible nature. Blockchain technology represents a similar infrastructure level—most valuable when shared, open, and permissionless. Organisations should no more demand "their own blockchain" than they would demand "their own internet."

---

## 2. The Blockchain: Architecture of Trust in an Open Network

The prevailing confusion in regulatory and institutional discourse stems from a fundamental misunderstanding of what constitutes a "blockchain." It is frequently assumed that any database utilising a chain of blocks for data storage is, by definition, a blockchain. This reductionist view has led to a perceived close relationship between "permissioned DLT" and blockchain technology, endowing centralised administrative systems with the unearned reputation for security and immutability that belongs exclusively to decentralised public networks.

### 2.1 The "Chain of Blocks" Fallacy

The "chain of blocks" data structure—where each batch of records is increasingly linked to the previous one via cryptographic hashing—is not the defining innovation of blockchain technology. This method of ensuring data integrity was pioneered by Stuart Haber and W. Scott Stornetta in 1991, nearly two decades before the invention of Bitcoin.[@NKREGHHJ]

It is crucial to understand precisely what a chain of blocks achieves: it provides tamper-evidence, not immutability. The cryptographic links ensure that if any historical record is altered, the links to all subsequent blocks are broken, making the modification detectable. However, the data structure itself does nothing to *prevent* such alteration. In a system controlled by an administrator (as in all permissioned DLTs, be it a sole entity or a collective body), the administrator possesses both the technical capability and the authority to rewrite the chain. They can alter a past record, re-calculate the hashes for all subsequent blocks, and present this new chain as the valid version. The chain remains internally consistent, but history has been rewritten.

Therefore, the presence of a "chain of blocks" in permissioned DLT does not confer the security properties associated with Bitcoin or Ethereum. It merely provides a method for auditing the database—provided one trusts the auditor.

### 2.2 The Defining Role of Open Competitive Consensus

Satoshi Nakamoto’s breakthrough in 2008 was not the invention of the chain of blocks, but the combination of the known data structure with a mechanism for decentralised node synchronisation—the open competitive consensus protocol (Proof-of-Work).

In a public permissionless blockchain, there is no administrator to dictate the state of the ledger. Instead, the network relies on an open competition where independent nodes (miners or validators) expend resources to propose the next block. This process is often misunderstood merely as the "production of cryptocurrency." In reality, it is a sophisticated method of synchronising a distributed ledger in the absence of a central authority.

What elevates a mere chain of blocks to the status of The Blockchain is this open, permissionless consensus. It transforms the ledger from a passive record kept by an administrator into an active, self-securing organism. Because the right to append to the ledger is distributed among thousands of competing, non-colluding actors, no single entity can dictate the truth or rewrite history.

### 2.3 From Cryptocurrency to Decentralised Platform

It is a common misconception that blockchain technology was exclusively designed for, and is limited to, the circulation of digital currency. However, the potential for using this infrastructure as a general-purpose public repository was embedded in the system from its very inception.

In the first block of the Bitcoin blockchain (the "Genesis Block"), Satoshi Nakamoto included a text message: *"The Times 03/Jan/2009 Chancellor on brink of second bailout for banks."*[@7WEZBU3E] While politically symbolic, technically this served as a proof-of-existence, anchoring the data to a specific moment in time. This act demonstrated that the blockchain could serve as an immutable public noticeboard.

Over the following years, users began to exploit this property to secure various forms of arbitrary data—messages, images, and computer code—directly into the Bitcoin blockchain. As detailed by Sward, Vecna, and Stonedahl in their study *Data Insertion in Bitcoin's Blockchain*, gigabytes of non-financial data have been permanently embedded in the ledger, effectively turning Bitcoin into a censorship-resistant global hard drive.[@7WEZBU3E]

This capability evolved into one of the first protocols for tokenisation. The "Colored Coins" protocol[@BN8ZWCM5], for instance, allowed users to "flag" or "colour" specific fractions of Bitcoin to represent real-world assets or custom digital tokens. This was the precursor to the modern token economy.

Second-generation blockchains, most notably Ethereum, formalised this concept. Instead of shoehorning data into a payment ledger, they were explicitly architected to store and execute smart contracts—executable programs that run on the blockchain. In these systems, the code itself is published to the ledger, inheriting the same immutability as the financial transactions. This evolution transformed the blockchain from a simple calculator for money into a "World Computer"—a platform where not just value, but logic and applications, can be deployed securely and unstoppably.

### 2.4 Cryptocurrency as the Engine of Security

A frequent point of criticism is the role of cryptocurrency, often dismissed as speculative or unnecessary for government applications. This view ignores the structural necessity of the native asset. Cryptocurrency is not merely a payment token; it is the economic engine that secures the infrastructure.

The security model of a public blockchain operates on a virtuous cycle of economic incentives:

1. Usage & Fees: Users pay transaction fees in the native currency to use the network (e.g., to run smart contracts or transfer value).
2. Demand & Value: This utility creates demand, supporting the market value of the asset.
3. Incentivised Security: The value of the block reward attracts more miners/validators to compete.
4. Network Resilience: Increased participation raises the cost of attacking the network (e.g., hash rate in Bitcoin), making the ledger more secure and immutable.
5. Practical Immutability: As security scales, the ledger achieves practical immutability, attracting further high-value applications, thus renewing the cycle of usage and fee generation (Step 1).

In contrast, permissioned DLTs lack this self-sustaining economic model. They rely on "authority" and external funding. There is no automated market force driving security up as usage grows; instead, scale increases administrative burden and centralisation risk. Only public blockchains harness open competition to convert economic value directly into digital security.

### 2.5 The DLT Classification Error and the Nature of Permissioned Systems

The term "Distributed Ledger Technology" (DLT) has become an unhelpful umbrella term that obscures critical distinctions. It groups together technologies that are diametrically opposed in their security models and operational logic. Classifying both Bitcoin and Hyperledger Fabric as "DLT" is akin to classifying both a rocket and a bicycle as "Transport." While technically true—both move objects from point A to point B—the grouping is practically useless. It fails to distinguish between an autonomous, universally accessible infrastructure secured by algorithmic consensus and a restricted, administrative tool dependent on institutional trust.

The distinguishing feature of permissioned ledgers—and the reason they differ so fundamentally from blockchains—is the mandatory presence of an administrative component. While configurations vary, the system remains conceptually closed. This is the direct opposite of a blockchain's permissionless architecture, where anyone can join the network on equal terms and it secures itself precisely because it is open and competitive. In this sense, "permissioned" is essentially a euphemism for "centralised" or "managed." The security model relies entirely on the perimeter defence of the network—controlling who can create and validate data.

In technical terms, a Byzantine Fault Tolerant (BFT) consensus protocol[@J8MVRXKA; @XG7F6ZQX] can create an architectural distribution of nodes, but the quality of being "distributed" is not the same as decentralised.[@X4ZJBGZ9; @UJPAXCD5] It should be noted that "decentralisation" can exist only among the privileged entities that have been admitted, but having that it also goes with caveats. The control over network admission (membership services) usually remains a critical central point of failure.

In cases where the network is managed by a single administrator, the system is fundamentally centralised. Possessing the authority to issue and revoke certificates grants the administrator the capability to control the network's reality. If they can revoke the credentials of dissenting nodes, they can effectively rewrite the ledger. In such a scenario, the consensus mechanism serves merely as an internal consistency check; it would be a misconception to pass such a system off as decentralised.

Consequently, permissioned systems confront a fundamental scalability paradox. To achieve genuine resilience against cyberattacks, a network requires a vast number of independent nodes. However, in BFT consensus models (typically requiring a two-thirds majority, meaning they can tolerate *less than* one-third of nodes being malicious), security relies on the strict exclusion of malicious actors. While expanding the network raises the threshold for a successful attack, it exponentially increases the complexity of manual administration. A cohort of 50 nodes is administratively manageable but relatively vulnerable to compromise. Scaling to, say, 50,000 nodes—comparable to the scale of public blockchains like Bitcoin[@RB5E65RR]—might theoretically enhance security, but the administrative burden of vetting participants and enforcing cyber hygiene becomes insurmountable. This dynamic makes the infiltration of malicious actors inevitable, or alternatively, necessitates such rigid centralised control that the administrator itself becomes a single point of failure and the operational costs become prohibitive.

Even when configured for collective administration (a consortium), the system remains distinct from a blockchain. In these setups, the procedural complexity required to alter the ledger is often mistaken for immutability. However, because the ledger is controlled by a defined group of entities, it remains liable to collusion or collective coercion. While these initiatives are commonly termed "permissioned DLT," a more technically and politically accurate classification would be centralised systems with joint administration.

To achieve clarity, the taxonomy must be refined. A system should only be classified as a blockchain if it possesses:

1. Decentralisation: No central point of control or failure, be it a single or collective administration.
2. Open Competitive Consensus: A permissionless mechanism for state synchronisation.

Systems that lack these features are simply Distributed Databases or Permissioned Ledgers. They may have their uses, but they do not offer the specific value proposition of blockchain: trust minimisation and censorship resistance.

### 2.6 True Immutability vs. Tamper-Evidence

Finally, the misconception regarding immutability must be addressed. As established, a chain of blocks only offers tamper-evidence. Immutability—the practical impossibility of retrospective alteration—is a property that emerges only from the scale of public consensus.

In a permissioned system, the ledger is "immutable" only as long as the administrator (sole or a collective) decides it is. If the controlling entity is coerced, hacked, or acts with malicious intent, the ledger can be mutated. The "trust" in the system is ultimately trust in the defined number of entities running it.

In a mature public blockchain, the ledger is secured by thermodynamics (energy) or massive economic stake. To rewrite the history of Bitcoin would require an attacker to expend more energy than entire nations consume, a feat that is economically irrational and practically impossible. This is objective immutability, independent of human permission or administrative will.

Governments seeking a truly secure, unalterable registry for high-stakes data (such as land titles or digital currency) cannot rely on the "administrative promise" of permissioned DLT. They require the "architectural guarantee" of a public blockchain.

---

## 3. Misconceptions and Barriers to Public Blockchain Adoption

The reluctance of governments and financial institutions to embrace public blockchain infrastructure stems not from genuine technical limitations, but from a constellation of misconceptions that have achieved widespread acceptance despite lacking theoretical and empirical foundation. Having established the fundamental distinction between genuine blockchains and permissioned DLT systems, this section systematically addresses the persistent misconceptions and perceived barriers that have prevented institutional adoption, demonstrating that each supposed limitation is either misunderstood, localised, or readily manageable through appropriate technical and regulatory architecture.

These misconceptions are categorised into three areas: the fallacy that decentralisation implies a loss of governance control; unfounded fears regarding technical viability and security; and concerns regarding economic integration and legal compliance.

### 3.1 The Control Fallacy: Governance in a Decentralised Environment

A primary barrier to adoption is the fear that public means uncontrollable. This stems from a conflation of the infrastructure level, which must be uncontrolled to be secure, with the application level, which can and should be controlled for regulated use cases.

#### 3.1.1 Separating Infrastructure from Application

A fundamental source of confusion in blockchain discourse is the failure to distinguish between the infrastructure level (which includes the blockchain consensus mechanism) and the application level (smart contracts and decentralised applications). This distinction is not merely academic—it fundamentally determines what is possible, what is controlled by whom, and where regulatory authority can be exercised.

Due to the conflation of terms, properties of permissioned DLT are often mistakenly transferred to the blockchain. This is exemplified by the frequent question: "Who will run the nodes?" In permissioned systems, control over infrastructure implies control over applications, making the operator's identity critical. However, in public blockchains, this separation is architecturally absolute. Node operators have no mechanism to alter specific smart contracts. Therefore, the question of who runs the nodes is largely irrelevant; what matters is the network's aggregate decentralisation and security.

Public blockchains operate on two conceptually and technically distinct levels:

1. Infrastructure Level (Consensus): The network of nodes providing a secure, distributed, and immutable substrate for data storage and computation. The consensus mechanism, i.e. the protocol of synchronisation is trustless; no administrator controls the ledger.
2. Application Level (Smart Contracts): Where business logic resides. Smart contracts are programs deployed to the blockchain. Crucially, the business logic of a smart contract is independent and isolated from the infrastructure consensus mechanism.

This relationship is directly analogous to cloud computing: when a company deploys an application on AWS, Amazon provides the infrastructure but does not control the application's business logic. Similarly, blockchain nodes provide the computational substrate but cannot alter the code or logic of smart contracts deployed upon them. In fact, this separation is even more robust in blockchain, as no single node operator has the physical or legal capacity to interfere with a deployed application.

This architectural separation has critical implications for governments and regulated financial institutions. First, regulatory control is preserved, as a government deploying a digital currency as a smart contract retains complete authority over the application's business logic, encoding whatever administrative powers are required by law. Second, infrastructure is commoditised; governments simply use the network without needing to control the nodes. Finally, nodes act as service providers rather than governors; they confirm transactions for fees but have no authority over smart contract logic.

#### 3.1.2 The Trustless Paradox

Few terms in blockchain discourse have caused more confusion than trustless. Institutional decision-makers, upon hearing that blockchains are trustless systems, frequently conclude that such systems are unsuitable for regulated applications that inherently require trust, accountability, and legal authority. This conclusion rests on a fundamental misunderstanding of what trustless means in the blockchain context.

The term trustless, as applied to blockchain technology, has a specific and limited meaning: there is no trusted administrator at the infrastructure (consensus) level. The network does not rely on a central authority to validate transactions, maintain the ledger, or enforce rules. Instead, these functions are performed by a distributed network of independent nodes following a cryptographically enforced protocol. Critically, the term trustless applies only to the infrastructure level, not to the applications built upon it.

To illustrate, Ethereum's consensus mechanism is trustless—no individual or organisation controls which transactions are valid or can unilaterally alter the ledger. However, a smart contract application deployed on Ethereum can implement whatever trust model its designers choose, including highly centralised administrative control.

Smart contracts exist on a spectrum from fully trustless to highly permissioned. Fully trustless applications, often termed decentralised applications (dApps), are architected to operate without any administrative control or privileged roles. Examples include ERC-20 tokens where, once deployed, the token contract operates according to fixed rules, and decentralised exchanges such as Uniswap that operate through immutable smart contracts with no central operator.[@DT76CRF9][@7Q9ZTJPR] These applications leverage the unique capability of blockchain infrastructure to create economic coordination mechanisms that function independently of any trusted third party, a feat impossible in centralised systems where an administrator always retains ultimate control.

In permissioned and administered applications, conversely, smart contracts can and frequently do include extensive administrative controls. These grant designated addresses the authority to block or authorise specific transactions, freeze accounts pending legal process, and burn and re-issue tokens to rectify errors. Furthermore, these contracts can enforce compliance with regulatory requirements, such as identity verification, and manage intricate permission structures. These capabilities are intentional design features for applications requiring regulatory compliance and legal accountability. Critically, this administrative functionality is entirely transparent, with every action fully visible on the public blockchain ledger.

The blockchain development community has created numerous token standards specifically designed for regulated and security applications, codifying best practices for administrative control and compliance:

- ERC-3643 ("Tokeny"): A comprehensive standard for security tokens incorporating identity verification, transfer restrictions, compliance rules, and regulatory oversight mechanisms.[@ERC3643]
- ERC-884 ("Delaware Compliant"): Designed for tokens representing shares in Delaware corporations, including shareholder registry management and legal compliance mechanisms.[@ERC884]
- ERC-1400: A security token standard enabling granular transfer restrictions, document management, and partially fungible token classes.[@ERC1400]
- ERC-1594: Defines core security token functionality including transfer restrictions and regulatory compliance interfaces.[@ERC1594]

These standards demonstrate that tokenised securities and regulated financial instruments can be implemented on public blockchains whilst satisfying all regulatory requirements for oversight, compliance, and administrative control. The "trustless" nature of the underlying blockchain infrastructure does not prevent—and indeed, actively enables—the creation of highly regulated, permissioned applications at the smart contract level.

#### 3.1.3 Managed Immutability

A frequently cited objection to blockchain adoption for legal and regulated applications is the supposed immutability problem, i.e., because blockchain ledgers cannot be altered retrospectively, they are claimed to be unsuitable for real-world legal applications that require error correction, dispute resolution, or compliance with court orders. This objection reveals a profound misunderstanding both of how blockchains actually work and of how real-world legal registries actually function.

The objection to blockchain immutability rests on a false premise: that legal registries in the physical world routinely alter historical records retrospectively. They do not. Whether in land registries, corporate share registers, or the banking sector, the standard protocol is to append new entries rather than erase recorded past events. In banking and financial ledgers, for instance, when an erroneous transaction occurs, the institution does not delete the original record as if it never happened. Instead, it processes a correction transaction (or reversal), which is essentially a new transaction that rectifies the balance while preserving the audit trail. This ensures that the history of what occurred—including the error and its correction—remains transparent and auditable.

Public blockchain applications with an administrative component operate on this exact principle. While the underlying infrastructure level is immutable, the application level is designed to be updated via new transactions. Permissioned smart contracts and regulatory token standards effectively mirror the administrative capabilities of traditional systems, allowing designated administrators to freeze accounts, force-transfer assets, and burn or reissue tokens to correct errors. These actions are executed as new transactions that update the current state of ownership, fully complying with legal orders or operational requirements, without requiring any alteration of the immutable history. Properly designed smart contracts provide all necessary administrative flexibility whilst delivering unprecedented integrity guarantees.

#### 3.1.4 The Myth of Governing Chaos: Hard Forks and The DAO

The second significant network threat is conventionally considered to be hard forks—the spectre of the network splitting into incompatible chains, fragmenting the ecosystem and creating confusion about which chain represents the true ledger. The 2016 attack on 'The DAO'—a decentralised autonomous organisation running on Ethereum—is routinely invoked as evidence that public blockchains are subject to arbitrary and chaotic governance that makes them unsuitable for government applications. This characterisation profoundly misunderstands what hard forks are, how they occur, and what their implications actually are for applications built on blockchain infrastructure.

A hard fork is the creation of a new blockchain network that replicates the existing ledger, implementing a backwards-incompatible change to the blockchain's protocol rules. When the protocol is updated in a way that makes previously invalid blocks valid (or vice versa), nodes running the old software and nodes running the new software will diverge, potentially creating two separate chains and networks that operate them.

Hard forks occur for various reasons:

- Planned protocol upgrades: Most hard forks are scheduled, non-contentious improvements to the protocol, coordinated by the development community and widely supported by node operators
- Contentious governance disputes: Occasionally, disagreements about the blockchain's future direction lead to a lasting chain split, where a portion of the community continues operating the original protocol while others adopt the new rules
- Emergency responses: In rare cases, hard forks may be proposed in response to critical security vulnerabilities or major incidents (as with The DAO). A distinctive feature of such forks is their retroactive nature, as they can apply protocol changes retrospectively without necessarily altering the content of the blocks themselves.

**The DAO Case Study: What Actually Happened and the Lessons We Should Have Learned**

In June 2016, a vulnerability in "The DAO"—a smart contract application on Ethereum—was exploited, resulting in the unexpected acquisition of approximately 3.6 million ETH (valued at USD 50 million at the time) by a third party.[@7GQE7QXP] The Ethereum community faced a binary choice: uphold strict ledger immutability and allow the unexpected loss to stand, or execute a hard fork to reverse the unexpected loss and return funds to token holders. After extensive deliberation, a controversial hard fork was implemented, effectively invalidating the attacker's acquisition.

Crucially, a hardfork involves no coercion. In The DAO crisis response the node operators voluntarily elected to install new software, effectively initialising a new network that shared the ledger history up to the fork point. Those who dissented simply continued running the original protocol. Technically, a node implies no knowledge of alternative chains; it continues mining within its defined network. From a risk management perspective, this isolation is the solution itself. Any subset of nodes can, at any moment, replicate the ledger and fork the network—this is an inherent property of the technology.

Consequently, a portion of the community maintained the original chain, Ethereum Classic [@5PIBKG29]. Holders of digital assets prior to the fork found themselves with equivalent balances on both networks. While often dramatised, this duplication is manageable. This discussion sets aside the duplication of native cryptocurrency, as it serves merely as a utility fee mechanism with the scope of this study. What is really critical to examine is the issue of the replication in another network of applications earlier deployed and operated in the original network. However, this issue requires a more practical and pragmatic point of view, rather than dramatising it. The more pertinent analogy for a public registry application would be a hypothetical scenario where an actor copies a bank's database or a land registry to open a competing, unauthorised institution. Legal facts asserted by such an alternative operator would be legally void—akin to 'Monopoly money and its real estate cards'—or legally actionable as fraud (should the operator offer it as the original asset). In other words, the authority arises not from the network, but from the application administration. And the only valid question as a takeaway from The DAO crisis is whether there is a way to manage such situations more gracefully to ensure that, in the range of copies of the same application across a number of blockchain forks, only one is actually legally and technically valid. It appears it is not a problem, but rather a technical task for proper application design.

The deployment of blockchain technology for government purposes and for regulated markets requires a technical protocol for seamless application migration. Strategies for application continuity, similar to those for designing safeguards against network attacks, allow transferring an application from one blockchain to another. As detailed in the subsequent discussion on cross-blockchain public registries, this necessitates a technical and organisational framework for alienating compromised or technically obsolete chains and authoritatively designating new ones. The ultimate conclusion from The DAO incident is not that blockchains are fragile, but that forks are a standard property. Successful institutional adoption requires only a rigorous migration protocol: one that invalidates the application on the obsolete chain and re-instantiates it on the secure network.

### 3.2 Technical Viability: Security, Scale, and Privacy

All known threats and risks of blockchain are either localised or manageable. There is not a single problem in blockchain that cannot be adequately managed; there are only misconceptions about it. Reasonable application of blockchain technology should assume, as with any technology, the existence of a contingency plan. The logic that "someone might gain control over the network, therefore it cannot be used" is simply flawed. The same could be said of any technology. Risks must be managed.

For example, there exists a protocol for alienating a compromised blockchain from a blockchain-based registry, and together with backup and data migration protocols, it enables the ability to transfer user applications seamlessly to end users, even in the event of catastrophic network failure.

#### 3.2.1 The 51 Per Cent Attack: Economic and Social Realities

Perhaps no supposed vulnerability is cited more frequently in arguments against public blockchains than the "51% attack" (or "Majority attack"). The term has achieved memetic status in policy circles, invoked as a fatal flaw that disqualifies blockchain for critical applications. For mature networks such as Bitcoin and Ethereum, this risk is effectively a relic of the past.

A 51% attack occurs when a single entity gains control of more than half of a network's mining hash rate or staked assets. This provides a *probabilistic* advantage (e.g., a 51% chance vs. 49% chance) to produce the next block faster than the rest of the network combined. It does not grant deterministic control.

Critically, a 51% attacker cannot:
- Steal funds: Private keys remain cryptographically secure; an attacker cannot forge signatures or access wallets they do not control.
- Change core protocol rules: If an attacker attempts to enforce invalid rules (e.g., changing the monetary policy), they simply fork themselves off onto a worthless isolated chain. The rest of the network ignores them.
- Rewrite deep history: The computational cost of rewriting extensive history becomes prohibitively expensive instantly.

What an attacker *potentially* can do is limited to double-spending their *own* coins or temporarily censoring transactions. But even this is economically incoherent. To execute a double-spend attack, the attacker must secretly build a longer chain and then reorganise the ledger. The cost of this is astronomical:

- 2-block reorganisation: At Bitcoin's current hash rate, it would cost approximately $67 million in electricity (according to www.crypto51.app)[@RAD29358] just to revert the last ~20 minutes of history.
- 6-block reorganisation: To revert ~1 hour of history—the standard for high-value settlement—the cost increases exponentially, requiring days of sustained mining and hundreds of millions of dollars.

For perspective, spending $67 million to double-spend one's own tokens is economically irrational except in extraordinary circumstances. The attack would need to target a transaction of even greater value, severely limiting realistic scenarios. Moreover, such an attack would be immediately detected, triggering network responses that would render any stolen funds unspendable.

For Bitcoin, the probability of a successful attack has effectively become zero. Its hash rate exceeds 1000 exahashes per second (EH/s)[@UCZBVNZC]. Acquiring the hardware to capture even 30% of this would cost tens of billions of dollars and consume electricity comparable to a medium-sized nation. No entity—state or private—can deploy such infrastructure clandestinely. The capital would be far better employed mining honestly.

Similar logic applies to Ethereum. Post-Merge, an attacker would need to stake tens of billions of dollars in ETH. Once a block reaches checkpoint finality (approx. 12.8 minutes)[@FUBGDKQD], reorganising past that point requires the attacker to be "slashed"—meaning they would instantaneously lose billions of dollars of their staked assets. In the extreme scenario of an irrational nation-state attack, the human layer provides the ultimate backstop: social consensus. As demonstrated by the Ethereum Classic fork in 2020[@K224F324], exchanges and developers can simply coordinate to reject the attacker's chain.

The most compelling evidence is empirical: Bitcoin has operated for over 17 years with 100% uptime and zero successful 51% attacks. The hypothetical vulnerability is vastly less significant than the demonstrated, daily vulnerabilities of the permissioned and centralised databases that critics propose as alternatives.

#### 3.2.2 Bitcoin Application Primitives

The view of Bitcoin as solely a passive store of value is technologically obsolete. The network now functions as a robust, layered stack supporting complex, regulated applications while maintaining unmatched base-layer security.

Bitcoin represents the most reliable digital data repository ever created by humankind. It is not merely a secure storage value but a viable platform for applications. While the rise of Ethereum and its smart contracts has arguably overshadowed Bitcoin's capabilities in this regard, for those who are not deterred by higher transaction fees or longer confirmation times, Bitcoin offers an exceptionally reliable application environment.

There are historical incidents that are often cited to challenge this thesis of reliability. Specifically, the value overflow incident in 2010 [@RKZKWKAQ], where a bug created billions of bitcoin, and the accidental chain split in 2013 caused by a database version incompatibility (v0.7 versus v0.8) [@GH2MEVZK] are raised as evidence of potential failure.

However, a deeper analysis leads to a definitive conclusion: even during these events, the network never stopped. Mining continued, and transactions were processed without interruption. Consequently, there is no doubt regarding the statement that since its creation in January 2009, Bitcoin has maintained 100% uptime.

These incidents occurred during the early stages of the network's development. Far from undermining the system's reliability, the resolution of these crises demonstrated the network's resilience and flexibility. In both cases, the community and developers coordinated effectively to resolve the existential threats, proving the system's antifragility—its ability to survive and strengthen from shocks.

Second, these historical anomalies provide a crucial lesson for application architecture: no risk, however theoretical, should be entirely excluded. A robust application design must not rely blindly on the infallibility of the underlying layer but must include comprehensive contingency plans. As detailed in Section 4.6 of this paper, this includes protocols for backup, emergency suspension, and the migration of the entire application state to alternative infrastructure if necessary.

Regarding technical capabilities, modern upgrades have significantly expanded the toolkit. The Taproot upgrade [@PB53R7DR] enables complex spending conditions like multisig and time-locks to appear as standard transactions, enhancing privacy and efficiency. Ordinals [@XHD43K74] have transformed Bitcoin into a permanent data availability layer, allowing arbitrary data storage directly on the ledger without external dependencies.

Off-chain and client-side validation protocols like RGB [@MPUVHHI4] and Taproot Assets [@6K5IJDTK] shift business logic off-chain, verifying only cryptographic commitments on the mainnet. This is critical for regulated finance as it ensures absolute data privacy (observers see only opaque hashes) and unlimited scalability, as the network does not needlessly process every contract state change.

Furthermore, BitVM [@7MU3H86X] introduces optimistic verification, theoretically allowing Turing-complete smart contracts to be settled on Bitcoin. Simultaneously, the Lightning Network [@PFHZEA68] facilitates high-volume micropayments, enabling novel economic models like streaming money and machine-to-machine API monetisation.

For developers and governments, Bitcoin now offers a complete architecture: private, scalable execution anchored to the world's most secure and immutable digital record.

Furthermore, unlike the specialised Solidity language in Ethereum, application development on Bitcoin is not limited to any single programming language. Developers can utilise a wide range of familiar tools to build sophisticated systems [@EW6BIFIQ].

#### 3.2.3 Data Sovereignty and Privacy

Two related concerns frequently appear in policy discussions regarding blockchain adoption: data localisation requirements (regulatory mandates to store data within national borders) and privacy (protecting sensitive personal and commercial information). Both concerns reflect genuine regulatory requirements, but both are based on misconceptions about what data resides on-chain and how blockchain applications manage privacy.

Many jurisdictions impose data sovereignty and localisation requirements, particularly for government data and personal information. For blockchain transactions, this requirement is irrelevant. A corollary implication of blockchain architecture is often overlooked: because no sensitive data resides on-chain and the ledger is immutable regardless of node location, the geographical distribution of blockchain nodes poses no data sovereignty concern. Unlike permissioned systems requiring physical jurisdiction over servers, a government smart contract on Ethereum is secure regardless of the geographical location of the nodes. Attempts to enforce data localisation on the infrastructure level are technologically redundant; the blockchain is a global, borderless verification substrate, not a conventional data warehouse.

Data localisation requirements fundamentally address two vulnerabilities inherent to permissioned and centralised systems: data integrity and data leakage. While blockchain architecture inherently solves the integrity challenge through immutable consensus, ensuring data privacy requires deliberate application design. The misconception that public blockchains mean public data overlooks the distinction between ledger transparency and data privacy. Modern blockchain applications employ a tiered data architecture.

The first tier is on-chain public transaction data, which stores only the minimum data necessary for execution and verification. This consists of pseudonymous details such as cryptographic addresses, balances, and smart contract logic. These must be public to allow nodes to verify the legitimacy of ledger changes—ensuring, for instance, that a sender actually possesses the funds they are attempting to spend. No personal identifiers are recorded here. The second tier is off-chain private data, where sensitive identifiers like identity documents or legal contracts reside in secure, access-controlled databases.

The link between these tiers is established through anchoring: generating a unique cryptographic hash of a private document and recording it on the blockchain. This achieves privacy preservation, as the on-chain hash reveals nothing about the document's content, while also enabling integrity verification. Any party with access to the off-chain document can hash it and compare the result with the on-chain record to prove its authenticity. This architecture satisfies privacy regulations such as GDPR or equivalent frameworks by design; personal data never touches the public blockchain.

When blockchain infrastructure is preferred for its efficiency or integrity benefits, it can offer privacy features comparable or superior to traditional systems. Advanced cryptographic techniques, particularly Zero-Knowledge Proofs (ZKPs), allow a party to prove a statement is true without revealing the underlying information. Systems can be architected using view keys or selective disclosure credentials, whereby transactions are encrypted and opaque to the public, yet transparent to designated regulatory authorities holding the necessary decryption keys. This reconciles the traditional tension between commercial confidentiality and regulatory oversight.

Opponents concerning themselves with privacy often fail to acknowledge that this "problem" does not exist systemically—at least not to a degree that fundamentally impedes technological adoption. Empirical evidence supports this: the crypto market has reached a capitalisation of over $4 trillion USD in October 2025[@FEK4473X] despite the supposed privacy defects. The booming DeFi sector is a testament to this reality: such a sophisticated financial ecosystem would not have scaled to manage hundreds of billions of dollars if fundamental privacy flaws rendered it unusable.

#### 3.2.4 The Scalability Myth: Multi-Chain Architecture

A third frequently cited objection to public blockchain adoption is limited transaction throughput. The claim is straightforward: Bitcoin processes approximately 7 transactions per second (TPS), Ethereum processes roughly 15–30 TPS, whilst centralised payment processors such as Visa can authorise over 65,000 TPS.[@ZREJRWDE] The conclusion drawn is that public blockchains cannot scale to meet the demands of national payment systems. This objection rests on a false premise: there is no practical necessity to exclusively use one blockchain.

The blockchain ecosystem has evolved into a multi-chain environment where numerous independent networks operate concurrently. The appropriate architecture for large-scale government deployment is not to force all activity onto a single chain, but to distribute an application across multiple blockchains and utilise cross-chain protocols to enable interoperability. A multi-chain architecture bundling Bitcoin, Ethereum, Polygon, and Solana combines their individual capacities of 7 to 20, 30[@DT9E8XFD], 7,000[@88EFJ46E], and 65,000[@76TCZ3NR] transactions per second (TPS) respectively, to achieve an aggregate total throughput exceeding 72,000 TPS.

Global throughput serves millions of distinct users, and based on the principle of user choice, they will select their preferred blockchain. Market-driven fees will self-regulate the load, as users spread across networks based on speed, cost, and other preferences. This multi-chain architecture provides aggregate throughput that is effectively unlimited, as the system can scale horizontally by adding more chains. It also fosters market competition and drives innovation, whilst providing resilience and redundancy; if one blockchain experiences congestion, activity can shift to alternative chains without disruption. Finally, it ensures technology neutrality, as the government does not need to pick winners but instead defines interoperability standards.

While Layer 2 (L2) solutions are frequently proposed for scaling, they occupy a tier closer to centralised systems. Sidechains like Polygon PoS operate as separate, smaller private networks that execute transactions and store data on their own infrastructure, merely posting a cryptographic checkpoint (root hash) to Layer 1.[@UQ2SREGF][@DH9JDX2A][@Q6USZUW7] Due to this architecture, they are highly vulnerable; if the sidechain's nodes fail, the entire ledger could be irrevocably lost.[@XVNH35F6] In Rollups, technologies such as Arbitrum, Optimism, and zkSync offer a more robust model by executing transactions off-chain but regularly publishing compressed transaction data to Layer 1.[@VTNPVX5N] While this provides higher security than sidechains, it introduces a critical "window of vulnerability"—the delay between a transaction being accepted by the L2 sequencer and it being effectively published to Layer 1. During this window, if the sequencer is attacked or fails, the current operational data that has not yet been processed to Layer 1 can be lost.[@8MIGS88V] Hence, while Rollups stand higher in terms of security compared to centralised systems, they rely on a single point of failure for real-time data and possess a risk profile that is inferior to the redundant multi-chain architecture discussed previously. 

The supposed scalability problem is a non-issue when approached with the appropriate multi-chain architecture, which is already sufficient for current needs and growing rapidly.

### 3.3 Economic and Regulatory Integration

#### 3.3.1 The Cryptocurrency Volatility Myth

The concern regarding cryptocurrency price volatility is frequently overstated and relies on a misunderstanding of market dynamics. It is argued that because the price of assets such as Bitcoin or Ethereum fluctuates, they are unsuitable for stable government or commercial applications. This view conflates the asset's price with the cost of using the infrastructure.

First, for blockchain-based applications, the native cryptocurrency functions solely as a utility payment for transaction fees, e.g., in Ethereum known as gas. It is not the unit of account for the application itself. A government-issued digital dollar or a land registry smart contract operates with its own stable value; the underlying volatility of the fee token is irrelevant to the stability of the tokenised asset. The cryptocurrency is simply the fuel paid to the network to process the ledger entry.

Second, the mechanism of gas pricing on networks such as Ethereum represents a fair, open market mechanism. Whilst the price of block space may be volatile during periods of high demand, this volatility is a function of transparent supply and demand rather than arbitrary administrative pricing. In a permissioned DLT environment, pricing is determined by a closed consortium—effectively a cartel—which introduces the risks of rent-seeking and political gridlock. A volatile but open market is economically superior to a fixed but cartel-controlled price.

Finally, historical episodes of high volatility and transaction fees, such as during the CryptoKitties congestion or the 2020 DeFi summer, were not failures but catalytic market signals.[@B2DD3DWE] In a free market, these price spikes signalled an urgent need for greater capacity. This economic pressure directly drove the rapid development of alternative high-throughput Layer 1 blockchains such as Solana, Tron, BNB Chain, and the proliferation of Layer 2 scaling solutions. Far from stalling the market, this volatility forced an evolutionary leap in technology. Empirically, the problem turned into a long-term winning strategy, fostering a diverse, competitive, and highly scalable ecosystem that a centrally planned permissioned network could never replicate.

#### 3.3.2 Enforcing Sanctions and Ethics

A distinct category of concern involves ethical and geopolitical objections to transacting on public blockchains. Specifically, governments may be concerned that validators operating from sanctioned jurisdictions would earn transaction fees from processing government application transactions, potentially circumventing sanctions policy. This is a legitimate concern that requires a practical solution rather than the abandonment of public blockchain infrastructure. The solution relies on two mutually reinforcing mechanisms that effectively create a "clean" path for government transactions on open networks[@NBA3WJW9]:

1. **The Regulated Perimeter:** As further detailed in the proposed Cross-Blockchain Protocol for Public Registries, government applications operate within a technically closed, regulated perimeter deployed across a bundle of public blockchains. Within this perimeter, all entities—smart contracts, operators, and end-users—are strictly verified and whitelisted on-chain by respective government bodies or relevant regulatory authorities. This architecture allows the regulator to retain absolute control: any address suspected of violating Counter-Terrorism Financing (CTF) or sanctions rules can be immediately invalidated or frozen, effectively locking them out of the system.
2. **Authorised Mempool and Transaction Settlement:** To ensure transaction processing integrity, the system employs an alternative, authorised mempool mechanism. This routes transactions exclusively to compliant validators. While a user could mechanically bypass this and drop a transaction into the general public mempool—where a sanctioned node might theoretically include it in a block—the smart contract design prevents such a transaction from settling. The system detects the unauthorised processing path, meaning the transaction will not "finish" or effectuate the asset transfer. The violator fails to execute their intent, paying for the execution cost without result. The sanctioned validator processes the computation but fails to facilitate the regulated economic activity.

This approach ensures that while the infrastructure remains open and decentralised, the government's economic flows remain strictly contained within compliant channels.

#### 3.3.3 Competition and Market Structure

A final, often overlooked, concern with permissioned DLT systems is their potential to violate competition law and create anti-competitive market structures. This concern is particularly acute when permissioned ledgers are deployed by commercial consortia in competitive markets. Scrutiny from competition authorities globally—including the ACCC, the US Department of Justice, and the OECD—highlights that "closed" or "permissioned" networks can structurally facilitate cartel-like behaviour.

In Australia, regulatory scrutiny of such initiatives (e.g., by the ACCC regarding the ASX CHESS replacement) has underscored the necessity of "safe and effective competition" in clearing and settlement, warning against monopoly entrenchment and barriers to entry.[@FERA3G3H] Similarly, the OECD has explicitly identified the risks inherent in permissioned blockchains, warning that they can facilitate anti-competitive conduct through real-time exchange of sensitive strategic data, using technical standards to lock out new entrants, and collective "group boycotts" where members deny access to competitors.[@ZWD9NU8D]

The US Department of Justice has provided perhaps the most nuanced warning regarding this dichotomy. Assistant Attorney General Makan Delrahim, in his 2018 address "That's What I Call Music," acknowledged that blockchain technology holds transformative potential to increase efficiency and competition, citing the music licensing industry as a prime beneficiary. However, he explicitly warned that this same power creates a unique danger if implemented as "shared private ledgers" among competitors. He noted that such permissioned architectures allow competitors to police each other's behaviour and detect deviations from cartel agreements (e.g., price cutting), making collusion more stable and harder to break.[@D392X2KN] Thus, the very efficiency of the technology, if confined to a closed permissioned group, becomes a weapon for perfecting anti-competitive practices.

1. Inherent Collusion Mandated by Security: Permissioned DLTs, by design, rely on a closed validator set for security. This technical reality forces participating members—who are supposed to be fierce competitors—to agree on legal, organisational, and commercial terms. It structurally compels collusion, replacing market competition with necessary coordination.
2. Creation of an "Insider-Outsider" Market Structure: This mandated coordination creates a distinct "us versus them" dynamic. The consortium becomes a privileged club where members benefit from shared infrastructure while non-members are excluded, fundamentally altering the competitive landscape from an open market to a tiered system of privileged access.
3. Governance as a Tool for Exclusion: In this closed environment, governance decisions regarding fees, upgrades, and access are made collectively by incumbents. This power allows them to shape the market rules to their benefit, potentially stifling innovation and suppressing competition from non-members under the guise of "network management."
4. Illusion of Openness: While consortia often claim to have objective admission rules, these can easily serve as a facade for cartel-like exclusion. Whether these barriers are technically justified or are merely operational hurdles to protect incumbents is a serious question that demands rigorous investigation by competition bodies.

The European Union's Blockchain Observatory & Forum supports this view, flagging "private permissioned blockchains" as a primary source of antitrust liability. Unlike public blockchains, which are open access, permissioned consortia are viewed as potential "data pools" or "joint ventures" that require strict scrutiny to ensure they do not result in market foreclosure.[@PI76NP4W]

For governments implementing digital payments or tokenised asset platforms, the choice between permissioned DLT and public blockchains has competition law and other legal implications. If a government establishes or participates in a permissioned ledger consortium involving private sector participants (e.g., banks, payment providers), it must carefully assess competition impacts. Regulatory exemptions, oversight mechanisms, or structural safeguards may be required to avoid facilitating anti-competitive behaviour. Furthermore, there is a fundamental legal hurdle: when a government creates a DLT system to provide statutory services, it will likely encounter the need to first amend current laws. Typically, providing these services and maintaining the critical infrastructure is the exclusive role of a government agency. As previously discussed regarding centralised systems, the entity controlling the infrastructure practically controls the service, rendering them inseparable. Consequently, the admission of private actors into this infrastructure could violate existing statutory mandates. A relevant precedent is the privatisation of land registries in four Australian states, where state parliaments had to pass specific legislation to legitimise the transfer of titling and registry services from exclusive government office operations to private operators. Deploying government applications on public blockchain infrastructure avoids these concerns entirely. Unlike permissioned systems, public blockchains function as open infrastructure—akin to the internet—with no barriers to entry, no coordinated decision-making among competitors, and no privileged information sharing. Any firm can build complementary services or competing applications on equal footing. Consequently, the government's use of public blockchain infrastructure promotes competitive neutrality rather than advantaging particular market participants.

This consideration reinforces the broader argument: public blockchains align with good governance principles—transparency, competitive neutrality, and open markets—in ways that permissioned systems do not.

### 3.4 Conclusion: The Empirical Case for Adoption

The reluctance to adopt public blockchains is often framed as a matter of risk prudence, yet empirical evidence from government actions themselves tells a different story. Governments worldwide exhibit a stark contradiction between their stated scepticism of blockchain technology and their revealed preference through actual asset holdings. While policy discourse often characterises public blockchains as unreliable or unsuitable for institutional use, governments—particularly the United States, United Kingdom, and Germany—custody billions of dollars in crypto-assets, primarily derived from law enforcement seizures[@639ZRI2K]. Rather than immediately liquidating these "unsafe" assets, agencies maintain sophisticated infrastructure to secure them for extended periods, implicitly endorsing the reliability of the underlying technology.

This confidence extends beyond mere custody of seized assets. Some jurisdictions have moved toward strategic accumulation, exploring crypto-assets for foreign exchange reserves or international settlements. The logical inconsistency here is profound: if public blockchains like Bitcoin and Ethereum are sufficiently secure to hold billions in sovereign assets, they are robust enough to support government-issued digital currencies and tokenised assets. The 100 per cent uptime of Bitcoin over nearly 17 years and the secure management of state-held private keys empirically refute the narrative of technical fragility.

This revealed preference underscores a broader truth: the risks associated with public blockchains are manageable, while their benefits are unique and indispensable. The "problems" cited—governance, security, privacy, scalability—are either solved or manageable through the architecture of the application level. The choice is clear. Regulators and governments do not need to build their own "safe" but stagnant intranet of ledgers. They can, and should, confidently build their regulated applications on the secure, global, and innovative infrastructure of public blockchains.

## 4. Towards a Blockchain-Native Regulatory Architecture

### 4.1 Reframing the Role of the State

The preceding sections of this paper have dismantled the prevailing misconceptions surrounding public permissionless blockchains and have demonstrated how the supposed advantages of permissioned distributed ledger technologies rest on a foundation of flawed assumptions. Having established blockchain's superiority as infrastructure, what remains is the practical question: how can a government effectively harness this infrastructure for public registries, monetary systems, and regulated financial markets?

This is where the conversation must shift from debunking to design. This paper does not claim to offer a complete system architecture—that is a task worthy of its own treatise—but an overview of existing proposals and conceptual frameworks is essential to show that these solutions are not theoretical fantasies but practical, achievable realities.

The role of the state in a blockchain-enabled economy can be articulated across two primary dimensions. The first is on-chain governance of financial markets and capital markets. The second is the direct provision of public services on the blockchain. Both represent a paradigm shift that policymakers have been slow to embrace.

### 4.2 On-Chain Regulation: The Missing Paradigm

Few dispute that the state must retain its role as a regulator, regardless of whether market operators employ blockchain or permissioned ledger technologies. Yet the manner of that regulation is where current thinking falls tragically short. This paper advances a concept that fundamentally departs from existing approaches: on-chain regulation.

Traditional regulatory models—licensing, public registries, periodic reporting—were designed for a pre-digital age. When financial markets migrate to blockchain environments, regulators cannot simply continue wielding these analogue instruments and expect effective oversight. The entire paradigm must shift. Public registries and authorisation mechanisms must themselves be deployed on-chain.

Unfortunately, this necessity is rarely acknowledged and even less frequently understood by policymakers. Bureaucratic inertia favours the familiar, and the familiar will ultimately strangle innovation. A regulator who issues a paper licence to a digital asset operator is not regulating the digital economy—they are merely erecting paper obstacles to it.

What makes blockchain transformative—transparency, finality, and algorithmically deterministic execution of contract terms, collectively encapsulated in the notion of "programmable money" and "programmable economic relationships"—holds together only when all components exist within the same technological environment. The "magic" of smart contracts lies in their capacity to execute instant, intermediary-free exchanges: a property token for a payment token, settled atomically and irrevocably. One may design arbitrarily complex programmable economic arrangements, but the moment any component resides outside the blockchain environment, it becomes a bottleneck that can negate the entire system's efficiency.

### 4.3 Regulated Decentralised Finance: Three Pillars and a Permanent Formwork

A functional regulated digital economy rests upon three foundational pillars and a permanent formwork. Without any one of them, the promise of Web3 cannot be fully realised in a compliant, legally robust manner.[@VA5K97V5]

The Digital Token: The first pillar is the digital token representing property rights—be it a title token, a security token, or any other form of tokenised asset. The capacity to represent ownership and economic claims in a digital, transferable, programmable form is the sine qua non of the digital economy.

Digital Money: The second pillar is digital money. Whether this takes the form of stablecoins, central bank digital currencies, or other forms of public or private digital money is, in many respects, secondary. What is critical is that the money exists in the same technological environment as the digital token—that is, on the blockchain. An instant, intermediary-free exchange of a property token for a payment token is possible only if both exist on-chain.

Digital Identity: The third pillar is digital identity. Regulated markets require compliance. Due diligence cannot be an afterthought. While unregulated DeFi markets, sitting upon the first two pillars, may operate without identification, the anonymity of economic transactions in such environments facilitates criminal activity, financial fraud, money laundering, and terrorism financing.[@PIST872N]

Due diligence represents the first step in transforming the wild frontier of DeFi into civilised regulated markets. In the blockchain context, this may involve verification of addresses or the use of digital identity tokens. The specific implementation is a matter of design, but the principle is non-negotiable: participants in regulated markets must be identifiable.

On-Chain Regulation: The fourth component that makes it possible to properly set up the three pillars—on-chain regulation—is the architectural element that binds the other three together as a permanent formwork. In unregulated DeFi, anonymous addresses transact freely. In regulated DeFi, due diligence and compliance must be enforceable at the moment of transaction execution.

When a transaction is initiated, the smart contract must be capable of automatically validating all its elements. If the transaction involves a security token, the purchaser must have assurance that it was issued under a valid financial licence. If it involves a title token, the acquirer must know that it genuinely represents ownership of the underlying asset. When exchanging a digital token for digital money, the seller must be confident that they are receiving authorised currency, not counterfeit. And all parties must be able to verify each other's identities against legally prescribed standards.

If even one of these components is not on-chain, its validation becomes the bottleneck. At best, this introduces third-party validators into the transaction chain, slowing the system and increasing costs. At worst, it creates a single point of failure—a security vulnerability. Smart contracts can query only other smart contracts and on-chain data; they cannot directly access off-chain information.

Consider the scenario where a security token issuer obtains a paper licence. The smart contract has no knowledge of this. If the licensing authority maintains a centralised electronic registry, the problem persists. One might automate the process—programming software to query the regulator's registry before each transaction—but this does not address fault tolerance. No regulator can expose such a registry's API publicly; even a rudimentary distributed denial-of-service attack would render the system inoperable. The software queries the registry, the registry fails to respond, and the transaction cannot proceed.

The inevitable consequence is predictable: to mitigate this risk, regulators will restrict registry access to a handful of trusted operators, who will then serve as intermediaries—off-chain or on-chain "oracles"—creating precisely the centralised chokepoints that blockchain was designed to eliminate.

This is unnecessary. Blockchain's inherent properties of data integrity make it the only technological environment in which validation can occur without intermediaries and without API calls. For this to work, data concerning the validity of transaction elements must be on-chain, as must the authorities responsible for confirming that validity. If a governmental smart contract can be queried to confirm whether a given token is authorised for economic activity, whether a given digital dollar is valid, and whether a given digital identity has been verified according to legal requirements, transactions can proceed automatically in full legal compliance—without off-chain bureaucracy, paperwork, or third parties.

### 4.4 Advancing Regulatory Efficiency: Standardised Smart Contracts

The concept of on-chain regulation can be extended further. Consider the licensing of security token operators. An operator must obtain a licence to operate its custom designed security token smart contract, which is then recorded in a smart contract registry (e.g. maintained by the competent authority) as an authorised smart contract. But what if standardised smart contracts were developed, allowing an operator to deploy a pre-approved contract template and have it automatically registered in the governmental on-chain registry upon deployment—contingent only upon prior verification of the identities of all contract administrators?

In this model, the operator bypasses the laborious process of individual contract-by-contract licensing review. The regulator, in turn, retains the capacity to revoke authorisation: marking a smart contract as "invalid" in the registry smart contract ensures that any subsequent transaction verification involving that contract will fail. At the moment of transaction validation, the system simply rejects the transaction because the verification step—a call to the registry smart contract—is hardcoded into the contract logic.

### 4.5 Public Services on the Blockchain

The second dimension of state involvement extends beyond regulation to the direct provision of public services on the blockchain. This does not merely mean the passive oversight of privately operated financial smart contracts and private money; it means the active operation of public infrastructure.

A central bank could, for instance, issue digital currency, becoming a blockchain operator in its own right. This paper does not advocate for this outcome; its purpose is merely to demonstrate that such an endeavour is realistic and faces no insurmountable obstacles.

More generally, a prudent approach would see parallel operation of public registries—the companies register, the land registry, and others—both in traditional form and on the blockchain. This parallelism would provide a genuine impetus to the digital economy. Security tokens are a niche application; the larger prize lies in bringing core registries on-chain, as they represent the most economically significant assets: real property in the form of title tokens, corporate rights, intellectual property rights, and registrations of land, water, and air vehicles.

### 4.6 The Cross-Blockchain Protocol: Building Jurisdiction on Blockchain

The practical task of creating "jurisdiction on blockchain"—a regulated perimeter for public services and financial activity—is relatively straightforward. There is no practical necessity for governments to incur the extreme expense and time-consuming effort required to build new blockchains from scratch. Instead, the use of existing, battle-tested blockchains such as Bitcoin and Ethereum in a bundled architecture proves to be a superior choice, ensuring maximum reliability and fostering market competition between ecosystems.

While the previous sections established the superiority of public permissionless blockchains as infrastructure, the question remains: how does a government effectively utilise this infrastructure? The answer lies in adopting a protocol-centric approach that abstracts the underlying ledgers into a unified, agnostic database solution. This protocol is described in detail in the Cross-Blockchain Protocol for Public Registries [@EGN6WKZF]. Its essence is the creation of an abstraction level above individual blockchains.

#### 4.6.1 The Limitations of Naive Multi-Chain Approaches

In a simple single-chain system, regulators create registry smart contracts: authorised financial service operators, their smart contracts, verified (whitelisted) users admitted to the regulated perimeter, and so forth. In a naive multi-chain scenario, scaling is expansive: identical registries must be deployed on every blockchain permitted for regulated market activity. Such fragmentation inevitably demands intermediaries—third parties facilitating cross-chain transactions, often termed "orchestrators" in related literature[@DHBWXBBR].

Equally critical is the requirement for blockchain agnosticism. In practice, this means that at any moment, both operators and regulators must retain the option to abandon a blockchain or migrate applications to another. Immutability is an asset, but the loss of control over a smart contract can be irreversible. Any system will require root smart contracts or addresses from which trust cascades downward: all operating smart contracts within a given perimeter query the root for validation of the elements of the financial perimeter.

Multiple roots can and should be established to distribute risk—separate roots for digital money platforms, security tokens, and digital identity. Multi-level hierarchical root sequences enhance security; for example, a registry of security token smart contracts may be subdivided into specialised sub-registries. This, however, adds computational complexity and significantly increases gas costs. More fundamentally, all roots can potentially be compromised.

#### 4.6.2 The Overlaid Protocol

The ultimate solution is an overlaid protocol as described in the referenced paper. This protocol operates as follows: it is embedded within the user's wallet. The protocol is linked to a security certificate—using the same SSL certificates that authenticate websites and software on user devices, including governmental systems. The wallet does not become operational until it receives confirmation that the certificate administered by a governmental authority remains valid (not revoked). This is the first level of protection: a kill switch by which the governmental authority can halt all user wallets simultaneously if the system is compromised. Critical system updates are disseminated through this mechanism. Because the system is open source, anyone who chooses to build their own wallet—incorporating the protocol, which must also be open source—must download and install the certificate to launch the wallet.

The next level comprises root addresses and the public registries they administer. These registries contain knowledge about the validity of all system elements: operator addresses, their smart contracts, and so forth. The registry smart contracts themselves, and all transactions within them, occur on-chain—which, as discussed, is critical for system efficiency and security.

The protocol within the wallet reads ledger block data and constructs its own internal local database. This is important because not all blockchains maintain state; thus, the protocol also serves as a bridge to first-generation blockchain systems. For example, the protocol enables applications to be built on Bitcoin and connect it to the broader multi-chain ecosystem.

The technical protocol itself contains all the conditions for its operation and resides entirely within the wallet: which addresses serve as registry sources and how the index is formed. A wallet equipped with this protocol reads data from the blockchain and dynamically constructs the registry locally, updating it as new blocks are read.

A multi-chain system, say, comprising two blockchains, permits a unified registry spanning both chains. The closest analogy for understanding how this works is RAID disk arrays: blockchains are digital storage repositories unified by a RAID protocol[@ENNM8RZA]. Federated databases that construct indices from multiple sources are commonplace technologies—database sharding, for instance, in systems such as CockroachDB, Vitess, and Citus[@FCCVTH3P][@KWC4GGJG].

Linking multiple blockchains also enables registries of different specialisations to reside on different blockchains. A digital money registry might exist on one blockchain, while a security token registry exists on another. From the perspective of a wallet equipped with this protocol, the distribution of data across multiple blockchains poses no problem (no off-chain data bottleneck), as the wallet reads blocks from all blockchains in the link and maintains at all times an up-to-date picture of the validity of all elements within the regulated financial perimeter.

What does this offer the financial ecosystem? A regulator can choose the most reliable blockchain—Bitcoin—for maintaining a registry, without constraining operators to launch their dApps on Bitcoin. Operators may deploy on Polygon, for example, if it is included in the bundle of authorised blockchains. Such a registry of licensed security token smart contracts on Bitcoin might specify: Polygon, smart contract address, status—'valid' until such date (i.e., the term of the financial license).

Before executing a transaction, the user's wallet queries this database through the embedded protocol. Because, as noted, all registry data resides locally within the wallet, there is no threat from, say, a DDoS attack rendering an external database unavailable. Nor is there a risk of data substitution by a third party (man-in-the-middle attack), because registry data is read from the blockchain, meaning the wallet can obtain reliable information about the validity of all transaction elements and submit it to the blockchain for publication.

If a regulatory authority needs to invalidate a security token smart contract, an administrator sends an updating transaction (status: "invalid", or status: "migrated to" such-and-such contract). All wallets with this protocol read this update from the incoming block and locally update their registry, ensuring users can execute transactions at any time.

#### 4.6.3 Administrative Control Within Smart Contracts

A third level of control, as described above, is administration within the smart contracts themselves. If a user presents a court order requiring tokens held by one address to be transferred to a new owner, the administrator of that smart contract can execute a forced transfer, reissuance, or other actions.

In a more sophisticated scheme, also examined in the referenced paper, authorised governmental representatives can exercise mandatory administrative intervention inside smart contracts—not merely validation (enabling/disabling) of smart contracts, but deeper operational control.

In a deeper regulatory integration, the ability of government authorities to execute enforcement actions within smart contracts can also be implemented through the specified protocol, without even requiring administrative access at the smart contract level. At the same time, a security token operator may retain such access for routine administrative tasks.

Meanwhile, a state bailiff, for example, could mandate an amendment to the registry by creating an individual entry for a specific token—for instance, to block it. This can be done in a registry smart contract regardless of the blockchain on which the regulated tokens are located.

In a non-cross-platform scheme, a government body would need to maintain such a registry on every authorised blockchain; in this case, "computations" (validity verification) would be performed by the token smart contract calling the registry smart contract.

A cross-platform solution has different specifics. The token smart contract does not verify against the registry smart contract directly, which reduces "gas" costs. The protocol itself takes on the role of the validator—specifically, the wallet checks the validity of the token against its  overlaid database (registry) before sending, and rejects the transaction if the token has been declared invalid by an authorised body.

However, an interesting property emerges here. A user could still broadcast a transaction with such a token, intentionally bypassing the restrictive entry. To do this, they would use an unauthorised wallet to send the transaction directly to the network without checking the supplemental database. The transaction will be accepted because the smart contract itself does not perform verification; however, the operation involving the blocked token will not be reflected in the supplemental registry that tracks valid and invalid assets, meaning it will remain invalid.

A parallel from the real world suggests itself here. Parties are free to enter into any transaction. It is their conscious choice whether the transaction is lawful, and the system provides all the necessary conditions for that. But if the parties decide not to comply with legal requirements, such a transaction will simply be void.

The combination of these approaches—a configurable database built through publication and updates of data on the blockchain, together with smart contracts containing an administrative component—enables implementation of tasks of arbitrary complexity and any depth of governmental oversight.

#### 4.6.4 Cross-Chain Transactions Without Intermediaries

The cross-blockchain protocol permits transactions between different platforms and the transfer of assets and operations from one blockchain to another. There is no need for third-party "orchestrators" as contemplated, for exmaple, in the Project Acacia paper in Australia.

Most importantly, the protocol ensures maximum system security, as any blockchain within the link can be rejected (invalidated) if it is compromised, and all application data can be migrated to another blockchain. It is precisely the overlaid protocol above and the system of root addresses—which wallets trust—that makes this possible.

In the most pessimistic scenario, all blockchains can be rejected, or the certificate can be revoked, causing the wallet to consider no transactions valid—even as the blockchains themselves may continue to function (possibly in a compromised state).

### 4.7 The Governmental Mission

The tasks of governmental authorities in this framework reduce to the following:

1. Development and maintenance of the protocol and its updates. Just as the state provides critical elements of road infrastructure, the protocol is the "bridge" that the state must build and operate for regulated markets to function on blockchains.
2. Monitoring of blockchains for reliability. This includes, for example, monitoring the hash rate in Bitcoin to assess network security.
3. Inclusion and exclusion of blockchains from the bundle. Governance of the multi-chain ecosystem requires ongoing assessment and curation.
4. Maintenance of registries and support for root addresses and certificates. This ensures the functioning of regulated markets on the blockchain.
5. Unidirectional backup of data from all blockchains in the bundle. This is important for blockchains prone to forking, such as Bitcoin. Although orphan chains have become rare and brief due to high hash rates, backup remains a subtask of protocol maintenance.
6. Migration of registry and application data, using backup data where necessary. This includes migration to an alternative technological environment—for example, in the event of a complete abandonment of blockchain and reversion to closed centralised systems, or a partial reversion and reverse migration of certain services.
7. Ensuring fair competition in mining. While the state need not manage the infrastructure directly—its reliability derives precisely from the fact that no single entity controls it—risks of anticompetitive behaviour, including physical seizure of mining equipment, persist. Governmental powers are territorially limited, yet preventing monopolisation of blockchain infrastructure and protecting open competition are legitimate state functions.
8. Participation in mining or block validation by a governmental entity (optional). This serves as an additional measure to support competition within blockchain systems, alternative mempool health (the authorised mempool discussed in Section 3.3.2) and may exert a stabilising influence on the ecosystem.

### 4.8 The Role of Cryptocurrencies in Regulated Perimeters

Although this paper has emphasised the utilitarian role of cryptocurrency as the driving mechanism of blockchain infrastructure, it would be difficult to deny that cryptocurrency also constitutes economic value and is thus an object of economic relations.

Whether to admit cryptocurrencies into regulated perimeters is a matter of governmental policy. There are no technical reasons to exclude them. In favour of inclusion are the high liquidity of cryptocurrencies and their transnational character. The creation of a regulated financial perimeter is not only a technical, legal, and organisational undertaking but an economic one. Flooding the system with cryptocurrency would provide an influx of liquidity.

The question is the stringency of entry requirements. The strictest but most reliable scenario would admit only newly minted cryptocurrency, excluding coins with any prior involvement in money laundering or other illegal activities. The advantage of the proposed protocol is that it enables blacklisting of addresses and coins, effectively constituting a mechanism for external regulation and the combating of illicit activities in the cryptocurrency sphere. This mechanism counters grey-market exchangers and money laundering systems, rendering it valuable independently of any decision to deploy the regulated financial perimeter discussed above.

### 4.9 Conclusion: The Time to Act

As demonstrated, there are no obstacles to deploying blockchains in regulated financial perimeters. Mature conceptual frameworks exist for realising this vision. The mechanisms described here do not claim to be exhaustive or universally applicable; they require tailoring to the specificities of each jurisdiction and chosen governmental policy. What has been presented serves only to demonstrate that a rich spectrum of technologies and solutions exists, capable of supporting any strategic choice.

What remains certain is this: blockchains can provide digital infrastructure of exceptional reliability. With global capitalisation reaching $4 trillion USD in October 2025, it is increasingly difficult to ignore the opportunity to attract liquidity to domestic markets. But even this is not the decisive argument for adopting blockchain. Blockchains have become the epicentres of technological and economic innovation. Not closed permissioned systems, but rather open-source code and open competitive ecosystems represent the intrinsic value. Virtually everything we recognise in the space was born in this environment conducive to innovation, and this is the most compelling argument for a long-term strategic decision to transition to blockchain. To look at blockchains and act as if they are non-existent is a political blunder, to say the least. The choice is clear: embrace the proven, reliable, innovative infrastructure of public blockchains, or persist with the expensive, centralised, and ultimately futile experiment of permissioned ledgers. History will not look kindly on those who chose the latter.

---

## References
